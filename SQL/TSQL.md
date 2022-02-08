# TSQL #

## Updating Data Commands ##

These types of commands are for Updating Data

### MERGE ###

Used to determine what to do for existing tables / data sets

```TSQL
MERGE DestTable AS TARGET
USING SourceTable AS  SOURCE
ON (TARGET.ID = SOURCE.ForeignID)
WHEN MATCHED
THEN UPDATE SET
    TARGET.[Description] = SOURCE.[Description]
WHEN NOT MATCHED BY TARGET
THEN INSERT (
    [ID],
    [Description]
)
VALUES (
    [SOURCE].[ForeignID],
    [SOURCE].[Description],
    
)
WHEN NOT MATCHED BY SOURCE
THEN DELETE;

```

## Transactions ##

### @@TRANCOUNT ###

- Returns the depth level of transaction you are in (think begin tran... inception)
- Useful for handling transactions in the event of a failure or where nested transactions are possible
- Query @@TRANCOUNT to determine if there is an active transaction to commit, but in a catch block to determine if a tran needs to be rolled back