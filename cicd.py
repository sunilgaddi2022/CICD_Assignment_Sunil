
import git
import os

# Define the git 
git_url = 'https://github.com/Suraj-3029/ci-cd.git'

# Define the repository path
repo_path = "~\ci-cd"

# Define the branch to deploy
branch_to_deploy = "main"


# Clone the repository
def clone_repo():
    git.Repo.clone_from(git_url,
                           '~',
                           branch='main')

def pull_changes():
    # Pull the latest changes from the repository
    repo = git.Repo(repo_path)
    origin = repo.remote()
    origin.pull()
    print("Changes pulled successfully")
    
def deploy():
    os.system(' . ~/ci-cd/deploy.sh')
    print("deployed")

def check_for_new_commits():
    # Check if there are any new commits on the branch
    repo = git.Repo(repo_path)
    origin = repo.remote()
    origin.fetch()
    commits_behind = list(repo.iter_commits(f"HEAD..origin/{branch_to_deploy}"))
    return commits_behind

def main():
    #check if project exist
    is_path_exist = os.path.isdir('new_folder')
    if is_path_exist == False:
       clone_repo()
        
    # Check for new commits
    commits_behind = check_for_new_commits()
    if len(commits_behind) == 0:
        print("No new commits found. Skipping deployment.")
        return

    # Check if the specified branch is the latest
    repo = git.Repo(repo_path)
    current_branch = repo.active_branch.name
    if current_branch != branch_to_deploy:
        print(f"Skipping deployment as current branch is {current_branch}, not {branch_to_deploy}")
        return

    # Pull the latest changes from the repository
    pull_changes()

    #deploy the latest cahnges 
    deploy()

if __name__ == "__main__":
    main()