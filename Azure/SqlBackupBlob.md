## Overview

Need to backup SQL IaaS instance to Azure Blob Storage. Large Sql Backup, so it will need to be striped. Using Ola Halgren backup scripts.

## Best Practices

- For Sql 2016 or greater use Block Blob [doc][1]
- Use Shared Access Signature (SAS) to delegate access [doc][2]
- Use Ola Hallengren scripts to stand on the shoulders of giants [ola][4]
- From MS best practices [doc][5]
    - Unique file name for every backup
    - Set container access level to **private** so only users or accounts can read or write the blobs
    - Use a storage account in the same region as the virutal machine to avoid data transfer cost between regions
    - Periodic identification of failed backups and deleting the blob files [steps][6]
    - Use `WITH COMPRESSION` to minimize storage costs and transaction costs
    - Set `MAXTRANSFER SIZE` AND `BLOCKSIZE` arguments to [reccomended][1]

## Implementation

- Run Ola Hallengren Scripts to create Stored Procedures
- Create Storage Account and Container
    - Generate SAS KEY
    - Setup Lifecycle Management
        - Move from hot to cool after 24 hours
        - Delete after 30 days
- Create Credential From SAS Key

:exclamation: Do NOT keep the '?' at the front of the SAS key when creating the credential

- Test the backup sproc to URL with appropriate Max Transfer size and Block Size (keeping in mind the 50,000 block limit)
- Setup monitoring for failed backups
- Setup monitoring for Very Large Databases (VLDB) approaching storage limits (64 files * 200GB)
- Setup monitoring for SAS Key expiration and rotate accordingly


## Appendx

[1]: <https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url?view=sql-server-ver16> "Backup to URL for Microsoft Azure Blob (MS Doc)"

[2]: <https://docs.microsoft.com/en-us/rest/api/storageservices/delegate-access-with-shared-access-signature?redirectedfrom=MSDN> "Delegate Access with a Shared Access Signature"

[3]: <https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16> "Sql Backup and Restore Overview"

[4]: <https://ola.hallengren.com/sql-server-backup.html> "Ola Hallengren Backup Scripts"

[5]: <https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-best-practices-and-troubleshooting?view=sql-server-ver16> "Backup to URL best practices and troubleshooting"

[6]: <https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/deleting-backup-blob-files-with-active-leases?view=sql-server-ver16> "Deleting failed backup with active lease"

[7]: <https://www.domstamand.com/backing-up-sql-server-databases-to-blob-storage-using-impersonation/> "Sql Backup to Blob Using Impersonation"

[8]: <https://docs.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview> "Blob Access Tiers"

[9]: <https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restoring-from-backups-stored-in-microsoft-azure?view=sql-server-ver16> "Restoring Sql from Backups in Azure"

[10]: <https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-and-restore-with-microsoft-azure-blob-storage-service?view=sql-server-ver16> "Sql Back to Blob Overview"

[11]: <https://docs.microsoft.com/en-us/azure/storage/blobs/storage-performance-checklist> "Blob Storage Scalability Checklist"