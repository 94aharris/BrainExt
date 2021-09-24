# Azure Internal Load Balancer (ILB) #

## SNAT Behavior ##

Simple Network Address Translation is used on outbound traffic from the load balancer to route traffic to the appropriate backend pool member.

SNAT Port exhaustion is when backend instances run out of available SNAT port resources for that instances pool.

## ILB Hairpin (Internal Load Balancer Can't Call itself) ##

VM calling itself does not recognize both sides of the flow

The Azure ILB does not perform inbound Source-NAT (SNAT) so the original IP is preserved

When using the default LB rule setting, we do perform Destination NAT

![Azure ILB Hairpin](../images/ILB_Hairpin.png)

**Working Flow** from on prem through ILB to BE Pool Member

![Azure ILB Working on-prem to ILB](../Images/ILB_Working_Flow.png)

**Not Working Flow** from Azure BE Pool member through ILB to BE Pool Member

![Azure ILB Not Working Self back to self](../Images/ILB_NotWorking_Flow.png)


## Second NIC Workaround ##

* Create Additional (second) NIC for the VM
* Shutdown the VM
* Deallocate the VM
* Attach the second NIC
* Boot the VM
* Get the interface number
  * netsh int ipv4 show interfaces
* set the interface to not register with DNS
* create a static route for the ILB FE IP to go out the secondary NIC to the gateway


## Resources ##

* [Azure Load Balancer SNAT for outbound connections](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-outbound-connections#exhaustion)
* [Azure LB SNAT Explained](https://msazure.club/azure-load-balancer-snat-behavior-explained/)
* [Azure LB Problems: Accessing Internal LB frontend from particpating LB backend VM](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-backend-traffic#cause-4-accessing-the-internal-load-balancer-frontend-from-the-participating-load-balancer-backend-pool-vm)
* [Azure Internal Load Balancer Hairpin](https://cloudnetsec.blogspot.com/2019/08/azure-internal-load-balancer-ilb-hairpin.html)
* [Azure Application Gateway TLS](https://docs.microsoft.com/en-us/azure/application-gateway/ssl-overview)