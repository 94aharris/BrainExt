# Throubleshooting SQL #

## Resources ##

- [RedGate TroubleShooting SQL Server](https://assets.red-gate.com/community/books/troubleshooting-sql-server-accidental-dba.pdf)

## Early Analysis ##

### `sys.dm_os_wait_stats` ###

- Identify any major resource waits in the system and os level

### `sys.dm_io_virtual_file_stats` ###

- Evidence of high latency associated with read / write operations
- Tell how much I/O is being performed by SQL
- How the I/O load is distributed
- Can be used with Physical Disk\Avg. Disk Reads/sec and Physical Disk Avg

### sys.dm_exec_query_stats ###

- Investigate execution statistics for queries against database in plan cache
- Determine queries with highest accumulative reads, review associated execution plans

### Page Life Expectancy ###

- constant fluctuation in this an non-zero values for *Free List Stalls/sec* can indicate inadequately sized memory or queries are reading far too much data


## Symptoms ##

### high PAGEIOLATCH_SH waits ###

- indicates sessions are experiencing delays in obtaining a latch for a buffer page
- lots of sessions or one in particular are requesting a lot of data pages not available in the buffer pool
- I/O is needed to retrieve the data
- Does not neccessarily mean slow disk is the bottleneck it may just be the victim of excessive I/O caused elsewhere


## Locks ##

### Schema-m ###

- Schema modification
- Locks everything for the schema (Lifegaurds rotating shift everyone out of the pool)
