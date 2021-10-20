# Clustered Storage #

## Clustered Storage Notes ##

Storage Spaces and Storage Pools are a way to stripe disks together for increased performance and / or reliability in windows.

When a disk is created from a Storage Pool, it creates a virtual disk. If this is done after a VM is domain joined, the cluster makes the disk available to all nodes in a cluster.

The cluster manages disk access by using SCSI Persistent Reservations. This brings the disk online in a way that it is only writeable to a single node at a time.

Azure shared disks are supposed to support SCSI Persistent Reservations

Setting up a shared disk in cluster configuration requires at least 3 disks for quorum? (verify)

**Able to cause failure** by draining the secondary of all roles, pausing the secondary, then stopping the storage pool in cluster manager on the primary. When the secondary is still paused, the cluster pool won't come back online

- In the cluster, the physical disks show 'Becoming Ready'
- In File and Storage Services, the Physical disks show "Starting"
- Connect to the other node and run `Get-PhysicalDisk`.. there they are in a 'Starting' State
- Reboot the secondary node to release the reservations
- Still doesn't work, but comes back with time though
  
**Still Troubleshooting** seems like the disks coming back online is just time based

- ran `import-module FailoverClusters` and `Get-ClusterDiagnosticInfo` and saw some errors to investigate
- "Completing a failed non-ReadWrite SCSI SRB request"

Good Log source "Event Viewer\StorDiag\Microsoft-Windows-Storage-ClassPnP/Operational"

If both VMs deallocate, the loss can be catastrophic. In the event of a catastrophic failure...

1. Remove disk from cluster
2. Remove Pool from cluster
3. Open Elevated PowerShell on one of the nodes
   1. `Get-StoragePool -IsPrimordial $false | Set-StoragePool -IsReadOnly $false`
   2. `Get-VirtualDisk | Connect-VirtualDisk`
   3. `Get-Disk`
   4. `Set-Disk # -IsOffline $false`
4. Connect to the other node and repeat the actions to take ownership of the storage pool, get the virtual disk and, online
5. Add the storage pool back to Failover Cluster
6. Add the disk back to the Failover Cluster
7. Add the Disk back to the necessary resource (e.g. SQL)

**FFS** ... this is a terrible process

## Clustered Storage Links ##

- [MS Azure Shared Disk OVerview](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-shared)
  - Supports SCSI Persistent Reservations
- [Connect-VirtualDisk (Powershell)](https://docs.microsoft.com/en-us/powershell/module/storage/connect-virtualdisk?view=windowsserver2019-ps)
- [Get-StorageNode](https://docs.microsoft.com/en-us/powershell/module/storage/get-storagenode?view=windowsserver2019-ps)
- [Storage Spaces Disk States and Meanings](https://docs.microsoft.com/en-us/windows-server/storage/storage-spaces/storage-spaces-states)
- [Deploy Clustered Storage](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj822937(v=ws.11))
- [Storage Spaces FAQ](https://social.technet.microsoft.com/wiki/contents/articles/11382.storage-spaces-frequently-asked-questions-faq.aspx)
- [How the Cluster Service Reserves a Disk and brings a disk online](https://docs.microsoft.com/en-us/troubleshoot/windows-server/high-availability/cluster-service-reserves-brings-disk)

## Scrap Commands for Recreating Storage ##

CommandLine
-----------
get-storagepool -IsPrimordial $false | Set-StoragePool -IsReadOnly $false
Get-StoragePool -IsPrimordial $false | Remove-StoragePool
Get-PhysicalDisk -CanPool $true | Reset-PhysicalDisk
Import-Module FailoverClusters
Clear-ClusterDiskReservation 2
Clear-ClusterDiskReservation -Disk 2
Clear-ClusterDiskReservation -Disk 3
Clear-ClusterDiskReservation -Disk 5
Clear-ClusterDiskReservation -Disk 6
Clear-ClusterDiskReservation -Disk 1
New-VirtualDisk -FriendlyName "Data" -UseMaximumSize -ProvisioningType Fixed -ResiliencySettingName Simple -StoragePoolFriendlyName "DATA" -NumberOfColumns 1
Get-VirtualDisk
Get-VirtualDisk
$vd = Get-VirtualDisk
$vd | Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -UseMaximumSize -DriveLetter S | Format-Volume -FileSystem NTFS -UseLargeFRS -AllocationUnitSize 65536 -NewFileSystemLabel "Data"
$vd  | New-Partition -UseMaximumSize -DriveLetter S | Format-Volume -FileSystem NTFS -UseLargeFRS -AllocationUnitSize 65536 -NewFileSystemLabel "Data"
$vd  | New-Partition -UseMaximumSize -DriveLetter S | Format-Volume -FileSystem NTFS -UseLargeFRS -AllocationUnitSize 65536 -NewFileSystemLabel "Data"
Get-VirtualDisk
Get-VirtualDisk | Initialize-Disk -PartitionStyle GPT
Get-VirtualDisk
get-disk
New-Partition -UseMaximumSize -DiskNumber 6 -DriveLetter S | Format-Volume -FileSystem NTFS -UseLargeFRS -AllocationUnitSize 65536 -NewFileSystemLabel "Data"
New-Partition -UseMaximumSize -DiskNumber 6 -DriveLetter S | Format-Volume -FileSystem NTFS -UseLargeFRS -AllocationUnitSize 65536 -NewFileSystemLabel "Data"
Format-Volume -DriveLetter S -FileSystem NTFS -UseLargeFRS -AllocationUnitSize 65536 -NewFileSystemLabel "Data"
notepad
Get-PhysicalDisk