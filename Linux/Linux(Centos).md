# Centos Linux #

[How do I learn to be a Linux sysAdmin (iConrads)](https://www.reddit.com/r/redhat/comments/4y1qpe/red_hat_update_to_iconrads_how_do_i_learn_to_be_a/)

## Commands to know ##

- systemctl
- nmcli
- lsmod
- grep
- yum

## Mounting Disk ##

- [Mount Disk](https://codingbee.net/rhcsa/rhcsa-mounting-a-partition)

check disk mounts `lsblk`

check if disk is formatted with `blkid`

Mount the disk
`mount /dev/sdb1 /mnt`
 
Explore the disk 
`ls /mnt`
`df -h` - disk space overview

Unmount
`unmount /mnt`
or
`unmount /dev/sdb1`

## Reading NTFS ##

install the extra packages for enterprise linux

`yum install epel-release`

install ntfs-3g

`yum install ntfs-3g`

## Networking ##

See Networking Interfaces and connected / disconnected state

`nmcli d`

Restart an interface
* Disable 
  * `sudo ifdown <interfacename>`
* Enable
  * `sudo ifup <interfacename>`

Edit Network interface settings

`nano vi/etc/sysconfig/network-scripts/ifcfg-\<interfaceName\>`

Using a Centos Computer with a network connection to ethernet bridge one that does not have a network connection - [Bridging with Centos](https://fedoramagazine.org/internet-connection-sharing-networkmanager/)

1. Plug everything up
2. from the laptop computer check the state of the network interfaces and get devicename of ethernet
   1. `nmcli device`
   2. record device name for 'ethernet' TYPE (e.g. enp5s0)
3. Enable shared IPv4 Mode
   1. `nmcli connection add type ethernet ifname <DEVICENAME> ipv4.method shared con-name local`
4. Bring up the new local connection 
   1. `nmcli connection up local`
   2. `nmcli device`
   3. verify the Device Name now shows a 'connected' state with the Conection Name 'local'
5. On the receiving machine (e.g. server) bring up the ethernet interface
   1. `nmcli device`
   2. record ethernet device name
   3. `sudo ifup <devicename>`
   4. `nmcli device`
   5. verify the interface is Connected
  


# Updates / Installs #

Check for updates

`yum check update`

Update all

`yum update`
## Virtual Machines ##
[Install KVM on CentOS 8 Headless Server](https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-8-headless-server/)
[Install KVM on CentOS 7 Headless Server](https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-7-rhel-7-headless-server/)
