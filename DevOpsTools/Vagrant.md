# Vagrant #

**v**agrant is for **v**irtuals

Vagrant is a utility for provisioning and managing virtual machine environments. It does not do the configuration 'inside' the VM. See [Ansible](Ansible.md)

## Resources ##

- [Tutorials from Hashicorp](https://learn.hashicorp.com/vagrant)
- [Vagrant Cheetsheet](https://linuxacademy.com/site-content/uploads/2017/12/vagrant-cheatsheet-Linux-Academy.pdf)
  
## Basics ##

- Define a Vagrantfile
- cd into the folder with the file
- run execution with `vagrant up`

check for existing storage pools
- `virsh pool-list --all`