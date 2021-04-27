# Generally Useful Commands

## Quick PowerShell Hop Into Another Computer ##
    Enter-PsSession ServerName01
    #Alias
    etsn ServerName01
    [<servername01>]: exit

## See All Commands from Session ##
    get-history

## See all available keybindings ##
    ctrl+shift+alt+? 

## Tab Completion ##
*Tab Completion with Wild Cards*

`*keyword*`  + TAB

*Tab Completion with Menu*

`get-adl` + ctrl+space

![PSMenuCompletion](./../Images/PsMenuComplete.png)

## See Results Before Assigning to Variable ##
    Get-ChildItem | Tee-Object -Variable var
    ...output...
    $var
    ...output again...
    Get-ChildItem | Tee-Object -FilePath C:\temp\output.txt

## Trace-Command to debug ##
	Trace-Command * -Expression  {<thing to run i.e. script or cmdlet>} -PSHost

## Pivot to Drive With Alternate Creds ##
    net use \\server\share /user:<domain\username> <password>
    copy \\server\share\file.txt c:\temp\file.txt


## Remote COAF Fix ##
    Get-Item -Path HKLM:\system\CurrentControlSet\Control\Lsa\	
    Set-ItemProperty -Path HKLM:\system\CurrentControlSet\Control\Lsa\ -Name 'crashonauditfail' -Value 1

## Open explorer in current path ##
    invoke-item .
    ii.

## Enumerate Dictionary / Hash Table ##
    $hash = @{
        'key' = 'value'
    }

    foreach ($key in $hash.getEnumerator()) {
        Write-Host "$($key.name) = $($key.value)"
    }


## Manage Certificates ##
### Complete CSR Request ###
    Get-ChildItem Cert:\LocalMachine\My
    Import-Certificate -filepath "....\certname.cer" -CertStoreLocation Cert:\LocalMachine\My

### Export and Import Pub/Priv Key Pair ###
    $cert = Get-ChildItem Cert:\LocalMachine\My | Where {$_.FriendlyName -match 'friendlyname'}
    Export-PfxCertificate -cert $cert -FilePath c:\temp\cert.pfx -Password (Read-Host "enter pw" -AsSecureString)
    Copy c:\temp\cert.pfx \\remotesrv\c$\temp\cert.pfx
    etsn remotesrv
    Import-PfxCertificate -FilePath c:\temp\cert.pfx -CertStoreLocation Cert:\LocalMachine\My -Password (Read-Host "enter pw" -AsSecureString)