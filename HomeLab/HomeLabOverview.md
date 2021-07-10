# Home Lab Overview #

## Big Server ##

* Dell PowerEdge t605
  * [User Manual](https://downloads.dell.com/manuals/all-products/esuprt_ser_stor_net/esuprt_poweredge/poweredge-t605_owner%27s%20manual_en-us.pdf)
  * Specs
    * 24 GB RAM
    * 4 TB Disk Space
    * 2 Quad Core Processors
    * OS: Centos 7
  * Notes
    * Memory is not optimally configured, future state would be to get it in a good configuration
    * Windows Server 2012 is installed on a disconnected HDD
    * Need to install NTFS reader to read the other drives (onto Centos 7)

## Laptop ##
  
* Dell Something or other
  * Specs
    * 6 GB RAM
    * 1 TB Disk
    * OS: Centos 8 with Dual boot to Windows 10
  * Notes
    * Disk is starting to fail...
    * Battery is starting to fail...

## Networking ##

* Main internet from ISP to ONT to Router is hardwire
* Internet from router to Centos 8 Laptop is wireless
* Centos 8 Laptop shares internet via Ethernet connected to 1 GB switch
* Big server connects to 1GB switch and receives internet via bridge from Centos 8 Laptop

## Future ToDos & Notes ##

* Want to setup the Raspberry Pi (when I can find it) as a small single node
* Want to setup K8s (full kubernetes) maybe start with K3s to get feet wet
* Hardwire Internet to Lab switch from router (Maybe use over cable connection? 2.5 GB max but just the two nodes (router and endpoint switch))
* Run through the iCondors Linux Sysadmin Learning cirriculum
* Setup a larger K8s cluster with additional Raspberry Pi
* Find a way to host the BrainExt as a browseable and searchable website