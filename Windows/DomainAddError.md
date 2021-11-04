# Domain Add Error #

## Overview ##

Tried to take a computer joined in one domain, and move it to a different domain without deleting the original object in the source domain.

Domain join was successful, however there was an error on join ""Changing the Primary Domain DNS name of this computer to "" failed.  The name will remain "<newdomainname>".  Please check if "" is valid for the current domain."

When attempting to login with a domain account, the login fails that there is no trust relationship with the domain.

## Fix ##

Two options

1. Delete the computer object from the domain it was previously located in (or have an admin of that domain do it)
2. Rename the computer and join to the new domain with a new name