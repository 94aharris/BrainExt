# SCOM #

## On endpoint Server ##

- Stand up Server
- Ensure necessary FW rules are enabled
- Admin PowerShell to apply GPOs
  - `gpupdate /force`
  - Check `gpedit.msc`
    - [WSUS GPO](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/deploy/4-configure-group-policy-settings-for-automatic-updates)
    - **Computer Configuration > Policies > Administrative Templates > Windows components > Windows Update**
- Open *regedit*
- Check Windows Update Settings
  - `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`
    - *WUServer*
    - *WUStatusServer
  - If regkeys not set or not present try to set first
- Admin PowerShell
  - `wuaclt /detectnow`
- Check to see if the wuau (Windows Update) service is running
- Check the windows update logs
  - `Get-WindowsUpdateLog`
    - If error [symsrv.dll missing is reported](https://social.technet.microsoft.com/Forums/en-US/2e3caf57-e74f-44f8-8c4a-fe36650414fb/cannot-find-path-c65306program-fileswindows-defendersymsrvdll?forum=winservergen)
      - Search *C:\Windows\WinSxS* for the file and copy over to *C:\Program Files\Windows Defender*