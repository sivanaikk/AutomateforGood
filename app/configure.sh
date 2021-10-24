#!/bin/bash

node_name=$1
ip=$2
file=$3
user_name=$4
software_name=$5
#unzip /root/chef-starter.zip

cd /app/chef-repo/

#git init

#git add .

#git commit -m "Final" .

if [ $software_name == "server" ]
then
if [ $user_name == "ubuntu" ]
then 
software_name=apache
else
software_name=httpd
fi
fi

knife bootstrap $ip --connection-user $user_name --sudo -i /app/pem/$file --no-host-key-verify --node-name $node_name

knife node run_list add $node_name recipe[$software_name]

#knife supermarket install $software

#rm -rf cookbooks/starter

#rm cookbooks/chefignore

#knife upload cookbooks/*

#knife node run_list add $node_name recipe[$software]

ssh -i "/app/pem/$file" $user_name@$ip "sudo chef-client" 

echo "Successfully Installed"


knife node delete $node_name -y

knife client delete $node_name -y

#rm -rf /root/chef/chef-user/cookbooks/*

#echo "Successfully Done"
