# Azure SQL FCI #

## Storage Options ##

* Azure Shared Disks
* Storage Spaces Direct
* Premium File Share

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