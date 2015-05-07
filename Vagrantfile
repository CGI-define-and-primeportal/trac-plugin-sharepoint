# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
 set -e
 echo "Installing ansible"
 apt-get update
 apt-get install -y software-properties-common python-software-properties
 apt-add-repository ppa:ansible/ansible
 apt-get update
 apt-get install -y ansible
 echo "Running ansible"
 export PYTHONUNBUFFERED=1
 ansible-playbook -i localhost, \
                  --connection local \
                  /vagrant/develop.yml
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "Ubuntu precise 64 VirtualBox"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.provision "shell", inline: $script
  config.vm.synced_folder ".", "/vagrant", :create => true
  config.vm.network :forwarded_port, host: 10443, guest: 443
end
