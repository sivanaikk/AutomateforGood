#
# Cookbook:: apache
# Recipe:: default
#
# Copyright:: 2021, The Authors, All Rights Reserved.
package "apache2" do
  action :install

end
service "apache2" do
  action [:enable, :start]
end
file '/var/www/html/index.html' do
  content "Configured by AutoENV"
  action :create
end
