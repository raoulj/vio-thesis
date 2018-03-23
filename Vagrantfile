# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.box = "shadowrobot/ros-indigo-desktop-trusty64"
	config.vm.box_version = "0.1.0"
	config.vm.synced_folder "./data", "/home/vagrant/data"
	config.vm.synced_folder "./code", "/home/vagrant/code"

	config.vm.provider :virtualbox do |vb|
		vb.memory = 8192
	end

	# config.vm.provision "shell", path: "data/init.sh"

	config.ssh.forward_agent = true
	config.ssh.forward_x11 = true
end
