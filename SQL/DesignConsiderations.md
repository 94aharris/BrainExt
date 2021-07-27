# Design Considerations #

## One Database with Multiple Schema or Multiple Databases ##

- Are most users in the same location or using the same access path?
- Do the applications have the same administrative support staff?
- Do the applications have compatible availability requirements?
- Do the applications have compatible database and OS version requirements and upgrade paths?
- Are the applications reasonably similar in functionality and load characteristics?
- Do the appllications have the same usage level (e.g QA, development, production, maintenance, etc.)

## Resources ##

- [Microsoft SQL Server Index Architecture and Design Guide](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver15)
- [Checklist for Designing and Reviewing SQL Server Architecture](https://www.mssqltips.com/sqlservertip/3166/dbas-checklist-for-designing-and-reviewing-sql-server-system-architectures/)
- [SQL Server Database Design Best Practices Tutorial](https://www.mssqltips.com/sqlservertutorial/2900/sql-server-database-design-best-practices-tutorial/)
- [Microsoft Database Engine Tuning Advisor](https://docs.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver15)
- [Multiple Schema Versus Multiple Databases](https://www.oreilly.com/library/view/oracle-distributed-systems/1565924320/ch01s04.html)
- [Updated Kitchen Sink Query Example](https://www.sentryone.com/blog/aaronbertrand/backtobasics-updated-kitchen-sink-example)