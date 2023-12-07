#!/bin/bash

# take backup
source_folder="/var/www/html"
timestamp=$(date +"%d-%H-%M-%S")
tgz_file="backup-$timestamp.tgz.gz"
tar -czvf $tgz_file  $source_folder

#remove exist files
rm -rf  $source_folder

#copy new files
cp ~/ci-cd $source_folder

# restart the nginx server
sudo systemctl restart nginx