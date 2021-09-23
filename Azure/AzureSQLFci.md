# Azure SQL FCI #

## To-Do ##

What to do? Let try

* Azure Shared Disks
* Storage Spaces Direct

Get a cluster with each, try some graceful / bad failovers and stress test these guys.
Get some baseline #s.

## Storage Options ##

* Azure Shared Disks
  * Pros
  * Cons
* Storage Spaces Direct
  * Pros
  * Cons
* Premium File Share
  * Pros
  * Cons

## Performance Optimization ##

### Microsoft Azure SQL Cluster Checklist ###

* [ ] [Change Cluster Heartbeat Timeout](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/hadr-cluster-best-practices?tabs=windows2012#heartbeat-and-threshold)
* [ ] [Place VMs in Availability Set or Optimally Proximity Placement groups with accelerated networking](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/hadr-cluster-best-practices?tabs=windows2012#vm-availability-settings)
* [ ] Use a single NIC per cluster node and a single subnet
* [ ] [Configure Quorum Voting to use 3 or more odd number of votes](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/hadr-cluster-best-practices?tabs=windows2012#quorum-voting)
* [ ] Monitor Resource Limits (Disk, Mem, Drivers, etc.)
* [ ] [Validate sector size of VHDs before deploying your solution](https://support.microsoft.com/en-us/topic/kb3009974-fix-slow-synchronization-when-disks-have-different-sector-sizes-for-primary-and-secondary-replica-log-files-in-sql-server-ag-and-logshipping-environments-ed181bf3-ce80-b6d0-f268-34135711043c)
* [ ] Placing Virtual machine cluster nodes in separate Availability zones protects from datacenter-level failures
* [ ] Use Premium managed OS and data disks for VMs
* [ ] Configure each application tier into separate availability sets

### VM Size ###

* [ ] Use VM sizes with 4 or more vCPU
* [ ] Use memory optimized virtual machine sizes
* [ ] DSv2 11-15, Edsv4 series, M-, and Mv2- series offer optimal memory-to-vCore for OLTP workloads
* [ ] Collect target workloads performance characteristics and use them to determine VM size

### Storage ###

* [ ] Monitor the app and [determine storage bandwidth and latency requirements](https://docs.microsoft.com/en-us/azure/virtual-machines/premium-storage-performance#counters-to-measure-application-performance-requirements)
* [ ] Plan for highest uncached IOPS available and use data caching for data reads
* [ ] Place data, log, and tempdb files on separate drives
  * for data drive, only use premium P30 and P40 disks to ensure cache support
  * if submillisecond storage latency is require, use ultra disks for the transaction log
  * for M-series VMs consider the 'Write Accelerator' over ultra disks
* [ ] place tempdb on local ephemeral SSD (D\\) for most SQL workloads
* [ ] Stripe multiple Azure data disks using 'Storage Spaces' to increase I/O bandwidth up to the target virtual machine's IOPs and throughput limit
* [ ] Set Host Caching to read-only for data file disks
* [ ] Set Host Caching to none for log file disks
* [ ] Disable Azure geo-redundant storage and use LRS
* [ ] Format the data disk to use 64-KB allocation unit size for all data files placed on disks other than D:\\

### SQL Server Settings for Azure ###

These are **Generic** Reccomendations

* [ ] Enable database page compression
* [ ] Enable backup compression
* [ ] Enable instant file initialization for data files
* [ ] Limit autogrowth of the database
* [ ] Disable autoshrink of the database
* [ ] Disable autoclose of the database
* [ ] Move all databases to data disks, including system databases
* [ ] Move SQL Server error log and trace file directories to data disks
* [ ] Configure default backup and database file locations
* [ ] Set max SQL Server Memory limit to leave enough room for the OS
* [ ] Enable lock pages in memory
* [ ] Enable optimize for adhoc workloads for OLTP heavy environments
* [ ] Apply latest CUs
* [ ] Enable Query Store on all production SQL Server DBs
* [ ] Use reccommended number of files using multiple tempdb data files starting with one file per core up to eight files

These are **Azure Specific** Reccomendations

* [ ] Register with the SQL IaaS Agent Extension
* [ ] Leverage Azure backup and restore
* [ ] Ensure Accelerated Networking is enabled
* [ ] Leverage Security Center
* [ ] Leverage Azure Defender
* [ ] Leverage Azure Advisor
* [ ] Leverage Azure Monitor
* [ ] Implement HADR solution

### Proximity Placement Group ###

Place VMs in a [Proximity Placement Group](https://docs.microsoft.com/en-us/azure/virtual-machines/co-location#proximity-placement-groups) to keep VMs located together

Required for Azure Shared Disks

### Quorum Disk ###

Per Microsoft recommendations, a shared disk Quorum is recommended for shared disk FCI and is more resilient than a cloud quorum

* If you have a mount point from one shared cluster resource disk to another, ensure the disks are in the same group and the mounted disk resource is dependent on its source disk

### Mount Points ###

Not strictly necessary, but using mount points enables presenting multiple disks under a single root
- 
## Resources ##

* [Azure FCI Overview](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview)
* [Azure Quorum Disk](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/hadr-cluster-best-practices?tabs=windows2012#quorum)
* [Azure SQL HADR Best Practices](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/hadr-cluster-best-practices?tabs=windows2012)
* [Azure SQL VMs Performance Recommendations](https://docs.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist)
* [Determine Storage Bandwidth and Latency Requirments](https://docs.microsoft.com/en-us/azure/virtual-machines/premium-storage-performance#counters-to-measure-application-performance-requirements)
* [Azure Premium Storage: design for high performance calculations](https://docs.microsoft.com/en-us/azure/virtual-machines/premium-storage-performance#application-performance-requirements-checklist)
* [Make the most out of your Azure Disks using Storage Pools](https://blog.coeo.com/make-the-most-out-of-your-azure-disks-using-storage-pools)
* [Format SQL Disks with Use Large FRS to Avoid Check DBCC](https://www.codykonior.com/2017/10/18/are-your-disks-formatted-with-uselargefrs/)
* [Potential SQL Solution on Azure (Pros and Cons)](https://www.omegamadlab.com/sql-server-high-availability-solutions-on-azure-vms/)
* [Deploy Clustered Storage Spaces](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj822937(v=ws.11))
* [Configure Volume Mount Points for SQL Cluster](https://docs.microsoft.com/en-us/troubleshoot/windows-server/high-availability/configure-volume-mount-points-server-cluser)
* [Storage Spaces Disk Won't Pool](http://www.davidbarber.org/technology/storage_spaces.html)
* [Setup Cluster Disk Pool](https://www.ntfs.com/wss-how-to-set-up.htm)
* [Setup SQL on Failover Cluster](https://www.mssqltips.com/sqlservertip/6473/install-sql-server-2017-on-windows-server-2016-failover-cluster-part-1/)
* [Configure SQL Server TempDB on SSDs in Azure](https://www.sqlservice.se/configure-sql-server-tempdb-on-ssds-in-azure-virtual-machines-iaas/)
* [Disk Performance Testing](https://github.com/microsoft/diskspd)
* [Storage Considerations for Running in Azure](https://clusteringformeremortals.com/2019/05/02/storage-considerations-for-running-sql-server-in-azure/)
* [Shared Storage Options for Azure](https://thetechl33t.com/2020/11/04/shared-storage-options-in-azure-part-1-azure-shared-disks/)
* [SQL Stress Test](https://github.com/ErikEJ/SqlQueryStress)
* [How to Fake Loads with SQL Query Stress](https://www.brentozar.com/archive/2015/05/how-to-fake-load-tests-with-sqlquerystress/)