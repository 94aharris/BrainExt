# ArcGis Metrics #

## Steps ##

- Either programatically or manually get a token to use in requests
  - http://server[:port]/arcgis/admin/generateToken
  - Specify the web portal in the url field
- Navigate to the server subsite admin page and test the token
  - Run https://127.0.0.1/\<serversite\>/\<webadaptor\>/admin/usagereports?f=json
- Run a report to pull usage reports or logs
  - Usage reports can be used to see the site hits by product
  - Logs can be used to see specific user hits per product
  - Users may show as anonymous
- Programatically pull the JSON with the token in order to evaluate
- Upsert the pulled data into a sql table and perform some analysis
- Enrich the pulled data with additional context (User info from AD, user location, etc.)
- Wire up a visualization tool (e.g. PowerBi, Tableau, etc.) to the table and then use that for visualizing results


## Links ##

[Arcgis usage reports](https://developers.arcgis.com/rest/enterprise-administration/server/usagereports.htm)

[Arcgis Token Scripting PowerShell](https://enterprise.arcgis.com/en/server/10.8/administer/linux/scripting-languages-and-the-arcgis-rest-api.htm)