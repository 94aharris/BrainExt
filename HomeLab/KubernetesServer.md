# Kubernetes Server #

## Overview ##

Get my big server running Kernel Virtual Machines (KVM) so I can use it to host Kubernetes / Docker. This will be so I can spin things up / blow them away without a ton of reconfiguration, ton of Azure spend, or bunch of RaspberryPi's (currently).

I would like everything to be repeatable as much as possible (e.g. Ansible config or other) so the server isn't a snowflake. Essentially, I would like to wipe the server and repeat if needed.

- [Kubernetes Lab with KVM](https://medium.com/@nicholas.w.talbot/kubernetes-lab-with-kvm-8ab958cd3c5f)
- [Github Repo for Above](https://github.com/talbotfoundry/k8s-kvm)
- [Install KVM on CentOS/RHEL 7](https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-7-rhel-7-headless-server/)
- [Vagrant on Centos](https://www.vagrantup.com/downloads)
- [Setup Bridge on Centos](https://www.itzgeek.com/how-tos/mini-howtos/create-a-network-bridge-on-centos-7-rhel-7.html)

Everything is derived from the above gitrepo... but we're revising it for Centos as we go

**We're going to be converting this from Ubuntu to Centos Usage...OFC... LFG!**

* * * * * 
* * * * * 

# k8s-kvm
Upstream Kubernetes via KVM Vagrant and Ansible


# Project purpose

Create a "real" Kubernetes cluster on commodity hardware you might already have
at home or in the lab.  A lot of folks need something more substantial than than Mikiube
ie distinct hosts for the control plane and worker nodes, but don't want to pay
for the cloud all day long when using the cluster a few times a month.

## About

KVM is highly efficient allowing for a "real" kubernetes cluster to run on a single machine given a decent bit of CPU and RAM

This installation is targeted for a bare metal install on a machine hooked into a lab or home network.  
The master and worker nodes will have ip addresses on your network. This will allow you to interact with it like its a "real" cluster.

The cluster can be destroyed and created again easily as the networking configuration, Vagrantfile, and Ansible playbook only need to be configured once.  


# Pre-install requirements



## Pick some hardware

A bare metal machine (the kind that will hurt you if you kick it barefoot).  Do yourself a favor and plug it
into a physical network too (using a cord).  

An old workstation with multiple sockets is great (I used an seven year old Z600).
A NUC with 32GB RAM will do as well.  

Make sure you have at least 4 cores (not threads) and preferably more than 16GB RAM.
(16 will work, but just run two worker nodes).  Used hardware is great for this project.

Lastly do a **fresh** OS install.  NOT Tested with Ubuntu 18.04. **Now with Centos 7!**



## Identify a block of contiguous free ip addresses.

Kubernetes is IP address hungry, so make sure you have some on your network.

One is needed for the master and must end in 0.  Then one for each worker node starting with 1.  In the example I used 192.168.11.120 through 192.168.11.123 for a total of four addresses.

* * *

## Install dependencies for KVM ##

Add Additional Releases Channel
```
sudo yum install epel-release
```

Install Python3

```
sudo yum install python3
```

Install dependencies for headless KVM on CentOS 7
```
yum install qemu-kvm libvirt libvirt-python libguestfs-tools virt-install virt-manager bridge-utils
```

Install  Vagrant and libvirt plugin 

**Note : if [this vagrant bug](https://github.com/hashicorp/vagrant/issues/12445) is still open you'll need to use one of the resolution steps in the comments to get the vagrant-libvirt to work**

```
sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo

sudo yum -y install vagrant gcc libvirt-devel libxml2-devel make ruby-devel gcc-c++ libstdc++-devel

systemctl enable --now libvirtd

vagrant plugin install vagrant-libvirt
```
Install git
```
yum install git
```

Install Ansible
```
yum install ansible
```


* * *
## Pull down the Ansible Files From Github ##

Perform a clone from the github repo

```
mkdir /home/<uname>/Labfiles
cd /home/<uname>/Labfiles

git clone https://github.com/talbotfoundry/k8s-kvm.git

cd k8s-kvm
```

* * * 
## Start Up and Verify KVM ##

Start the libvirtd service
```
systemctl enable libvirtd
systemctl start libvertd
```

Verify KVM Loaded with lsmod and grep
```
lsmod | grep -i kvm
```

Validate hardware with a virt host validation. Investigate any FAIL
```
virt-host-validate
```

If you fail on the /dev/kvm exists
- verify you installed virt-manager
- **double verify** virtualization is enabled for the CPU in the bios

If you fail on 'load the fuse module'
- yum reinstall fuse -y
- sudo modprobe fuse

Verify network bridge

```
brctl show
virsh net-list
```

Attempt to intall the virtual machine

```
virt-install \
--virt-type=kvm \
--name centos7 \
--ram 2048 \
--vcpus=1 \
--os-variant=centos7.0 \
--cdrom=/var/lib/libvirt/boot/CentOS-7-x86_64-Minimal-1708.iso \
--network=bridge=br0,model=virtio \
--graphics vnc \
--disk path=/var/lib/libvirt/images/centos7.qcow2,size=40,bus=virtio,format=qcow2
```

* * * 

## Create a bridge

Create a file called "ifcfg-br0" in "/etc/sysconfig/network-scripts"

```
nano /etc/sysconfig/network-scripts/ifcfg-br0
```

Place the following in the file

```
DEVICE="br0"
BOOTPROTO="static"
IPADDR="10.42.0.56"
NETMASK="255.255.255.0"
GATEWAY="10.42.0.1"
DNS1="10.42.0.1"
ONBOOT="yes"
TYPE="Bridge"
NM_CONTROLLED="no"
```

determine the adapter you want to use for bridging

`nmcli d`

identify an adapter with network connection (e.g. enp9s0)

`nano /etc/sysconfig/network-scripts/ifcfg-enp9s0`

Add content

```
DEVICE=enp9s0
TYPE=Ethernet
BOOTPROTO=dhcp
ONBOOT=yes
NM_CONTROLLED=no
BRIDGE=br0
```

Restart the network

`systemctl restart network`

Double check everything with ifconfig the server will now be communicating over the br0 interface and `nmcli d` will show the device as 'unmanaged' since we set `NM_CONTROLLED=no`


# Installation

KVM needs to run as root, so go ahead and make yourself root

 
## Change the network prefix to the free address block you chose


 Open Vagrantfile with your favorite text editor.
 
 ```
cd cd /home/<uname>/Labfiles/k8s-kvm
nano Vagrantfile
 ```
 
 edit the following line.  Make sure you choose a network block that's good on your network.
 
 ```
 NETWORK_PREFIX="192.168.11.12"
 
```
 
## Edit alloted resources if desired

 Also in Vagrantfile.
 
 The number of worker nodes can be changed by editing the following line.  Total number of nodes will be the number of workers
 selected plus a master.  Two or three is recommended.
 
 ```
 NUM_NODES = 3
 ```

You change the allotted number of CPU cores and memory.  Be sure not to overallocate.

``` 
   config.vm.provider :libvirt do |libvirt|
    libvirt.cpus = 2
    libvirt.memory = 4096
```

## Run Vagrant
```
vagrant up
```
Your virtual machines should be created.  It may take several minutes to download the image the first time,
but it'll cache it in case you wish to rebuild the cluster.

***If* You get any screwy messages about image pool conflicts**, try running:

```
virsh pool-destroy images
virsh pool-delete images
virsh pool-undefine images
```


## Configure hosts for ansible

Get Ips for the VMs

```
virsh net-list
virsh net-info default
virsh net-dhcp-leases default
```

Look at this https://serverfault.com/questions/627238/kvm-libvirt-how-to-configure-static-guest-ip-addresses-on-the-virtualisation-ho

Edit hosts file
Make sure it has the correct ip address for the master starting with the ip address block you chose

Each node is an incrment of 1 from the master.  Add or delete worker nodes as needed depending on how many you chose.

```
[kube-masters]
master1.kube.local ansible_host=192.168.11.120

[kube-nodes]
worker1.kube.local ansible_host=192.168.11.121
worker2.kube.local ansible_host=192.168.11.122
worker3.kube.local ansible_host=192.168.11.123

[ubuntu:children]
kube-masters
kube-nodes
```

## Run ansible

This step takes several minutes even on a powerful host.  Initializing a kubernetes cluster is a non-trivial task.

You can run the tasks seperately **recommended for first time**:
```
ansible-playbook -i hosts bootstrap.yml
ansible-playbook -i hosts kube-masters.yml
ansible-playbook -i hosts kube-workers.yml
```


Or run them all together
```
ansible-playbook -i hosts kubernetes.yml
```

**NOTE: you will have to type "yes" several times as prompted to accept the rsa fingerprint for ssh!  Do it quick 
or its easy to get lost in the console** 


Output should look something like:
```
PLAY RECAP ***********************************************************************************************************************************************
master1.kube.local         : ok=24   changed=19   unreachable=0    failed=0
worker1.kube.local         : ok=19   changed=16   unreachable=0    failed=0
worker2.kube.local         : ok=19   changed=16   unreachable=0    failed=0
worker3.kube.local         : ok=19   changed=16   unreachable=0    failed=0
```


## SSH to the master node
```ssh kube@192.168.11.120```

Change the ip address to whatever you made the master.  The default username / password is kube / kubernetes



 ## Add kubernetes network plugin
 
 ```
 kubectl get nodes
 ```
 
 The nodes will show not ready until you install a network plugin.
 
 ```
 kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.11.0/Documentation/kube-flannel.yml
 ```
 
 ## Smoke testing cluster
 
 
 
 ```
 kubectl get nodes
 kubectl create deployment nginx --image=nginx
 kubectl create service nodeport nginx --tcp=80:80
 kubectl describe service nginx
```

# Rebooting the cluster

Building the VM's with KVM and using a host bridge allows the cluster to be torn
down and brought back up quite easily.  This is great when you want to start fresh.

## Kill the old cluster

Destroy VM's through Vagrant
```vagrant destroy```

Kill the host ssh key fingerprint cache
```rm ~/.ssh/known_hosts```

## Make the cluster again

Run the vagrant up command

Run ansible again

Install Kubernetes networking

# Housekeeping items

## Setup kubectl on your machine

Grab the config and keys from the .kube/config file in the kube user's home directory
on the master.  Add them to the .kube/config file on your machine with kubectl.


### Check the status of your VM's

```
root@z600:~/k8s-kvm# virsh list --all
 Id    Name                           State
----------------------------------------------------
 1     k8s-kvm_worker-3               running
 2     k8s-kvm_worker-1               running
 3     k8s-kvm_worker-2               running
 4     k8s-kvm_master1                running

```




