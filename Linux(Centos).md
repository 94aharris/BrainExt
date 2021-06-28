# Centos Linux #

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

