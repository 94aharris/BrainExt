# Centos Linux #

[How do I learn to be a Linux sysAdmin (iConrads)](https://www.reddit.com/r/redhat/comments/4y1qpe/red_hat_update_to_iconrads_how_do_i_learn_to_be_a/)
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

Using a Centos Computer with a network connection to ethernet bridge one that does not have a network connection - [Bridging with Centos](https://access.redhat.com/solutions/3017441)

<<<<<<< HEAD:Linux(Centos).md

# Updates / Installs #

Check for updates

`yum check update`

Update all

`yum update`
=======
## Virtual Machines ##
[Install KVM on CentOS 8 Headless Server](https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-8-headless-server/)
[Install KVM on CentOS 7 Headless Server](https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-7-rhel-7-headless-server/)
>>>>>>> c36bd5b5faf981c790b3eb69ccc69f096aef5adc:Linux/Linux(Centos).md
