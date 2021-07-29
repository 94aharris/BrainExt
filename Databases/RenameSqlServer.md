# Renaming a Server Hosting SQL #

## Links ##
[MS Docs](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/rename-a-computer-that-hosts-a-stand-alone-instance-of-sql-server?view=sql-server-ver15)

## Steps ##
1. Ensure that a certificate has been requested and updated containing the new name for secure SQL comms
2. Have DNS create the new A Record
3. Rename the Server
4. Have DNS drop the old A Record
5. Have DNS create the CNAME pointing to the New A Record
6. Check the old name using the SQL `SELECT @@SERVERNAME AS 'Server Name';`
7. Run the following SQL

        EXEC sp_dropserver '<old_name>';  
        GO  
        EXEC sp_addserver '<new_name>', local;  
        GO  

8. Restart SQL Server (service)
9. Verify the new name with `SELECT @@SERVERNAME AS 'Server Name';`

