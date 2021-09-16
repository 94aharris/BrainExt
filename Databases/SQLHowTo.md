# SQL How To #

## Declare a User Defined Table as a Scalar Variable ##

```sql

DECLARE @scalarTable AS GenericTable_INT

INSERT INTO @scalarTable
VALUES (1)

INSERT INTO @scalarTable
    SELECT PK FROM [dbo].[othertable] where col like '%value'
```


## How To Links ##

- [Configure A Server to Listen on a Specific Port](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-a-server-to-listen-on-a-specific-tcp-port?view=sql-server-ver15)