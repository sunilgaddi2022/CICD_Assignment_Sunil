# ci-cd

a sample python code to perform ci-cd 

**Repo setup:**

>create a folder called ci-cd*
>mkdir ci-cd

>touch index.html<br>
    hello world

>touch cicd.py<br>
    integrate git python 

*script to deply*
>touch deploy.sh

take a backup<br>
remove exist files in var/www/html<br>
copy new files from ~ci-cd to /var/www/html<br>
restart nginx

**lunch a ec2 instance**
>sudo apt update<br>
>sudo apt install nginx<br>
>sudo pip install GitPython<br>
>sudo crontab -e<br>
    * * * * * python ~/ci-cd/cicd.py
