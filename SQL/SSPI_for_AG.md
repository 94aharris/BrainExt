# SSPI for Availability Group #

## Link ##
* [Configure Kerberos for Avvailability Groupos](https://blog.coeo.com/configure-kerberos-for-availability-groups)

## Notes ##

BLUF: **To allow kerberos auth you need to create Server Principal Names for the SQL Servers and the AG listener for both the instance name and the listening ports for the service account**

* assumptions
  * SQL Server 2016
  * SQL is running on 1433
  * Listener is running on 5100
* Create SPN for 
  * domain\sqlserviceacct
    * MSSQLSvc/node1.domain.com:1433
    * MSSQLSvc/node2.domain.com:MSSQL2016
    * MSSQLSvc/node2.domain.com:1433
    * MSSQLSvc/node2.domain.com:1433
    * MSSQLSvc/SQLAG:1433
    * MSSQLSvc/SQLAG.domain.com:1433
    * MSSQLSvc/SQLAG:MSSQL2016
    * MSSQLSvc/SQLAG:5100
    * MSSQLSvc/SQLAG.domain.com:5100
    * MSSQLSvc/SQLAG.domain.com:MSSQL2016