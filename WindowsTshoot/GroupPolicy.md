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
