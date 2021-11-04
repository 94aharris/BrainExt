# Group Policy #

## GPResult ##

See existing group policy from a computer

```powershell
# User and computer policy in console
gpresult /r

# Computer onlly policy
gpresult /r /scope computer

# save as html to file
gpresult /r /h gpreport.html
```


## GPUpdate ##

- [How GPUpdate Works](https://adamtheautomator.com/gpupdate/)

- Synchronous (one at a time) GPUpdate targeting computer policies
  - `gpupdate /force /target:computer /sync`

## NLA Messiness ##

-- Observations --

Gpupdate /force on causes ping drops / disconnects for about 7 seconds from 18:31:53.180 -  18:32:01.638


During that timeframe, a notable activity that occurs (from procmon) is that Network Location Awareness kicks in (NLA)


-- Research / Findings --

Network Location Awareness can cause a Network profile to switch from Domain -> Public and is based on DNS discovery. This makes sense why making changes that force DNS resolution affects the issue.

Article Find 
Network Location Awareness doesn't identify domain - https://www.mcbsys.com/blog/2018/03/network-location-awareness-doesnt-identify-domain/ (TLDR at the bottom with fixes)

Supporting Articles
How Network Location Awareness Service Can Ruin Your Day (Fix) -- https://newsignature.com/articles/network-location-awareness-service-can-ruin-day-fix/
Remote Site FW problem, PCs go from Domain to Public Provile - https://community.spiceworks.com/topic/2238718-remote-site-new-fw-problem-and-poof-pc-s-go-from-domain-to-public-profile

Potential Fixes

Set the NLA service to "Automatic (Delayed Start)" and only when the network is available.
sc config NlaSvc start= delayed-auto
sc triggerinfo NlaSvc start/networkon stop/networkoff
sc qc NlaSvc
sc qtriggerinfo NlaSvc
Set the Connection Specific DNS Name to match the domain controllers local domain. This can be set in network connections or in Group Policy.

