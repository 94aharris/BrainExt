# App Insights #

## Links ##
* [Add App Insights to Angular SPA](https://devblogs.microsoft.com/premier-developer/angular-how-to-add-application-insights-to-an-angular-spa/)
* [Application Insights to JavaScript](https://docs.microsoft.com/en-us/azure/azure-monitor/app/javascript)
* [Add App Insights to Angular ..different take](https://www.c-sharpcorner.com/article/how-to-integrate-azure-application-insights-service-to-an-angular-application/)
* [Add App Insights to Angular yet another way](https://onthecode.co.uk/monitoring-live-angular-apps-with-azure-application-insights/) 
  * Got it working this way



## Notes ##
* 'Workspace Based' requires log analytics workspace
* Buffers user sessions so data not sent back to MS until page is closed
* Can use trace and log analytics


## Angular Single Page App (SPA) Notes ##
* Add instrumentation key to environments constants
* Add the application insights npm dependency
* Create a folder *app\shared* if it does not already exist
* Create `logger.service.ts` and use as a typescript wrapper around teh application insights javascript api
  * Make sure you import what's needed from ngCore
* Add the MonitoringService to the app constructor
* Add the MonitoringService Provider to the module .ts
* By default, application insights will not track state based routing changes must enable for angular in object creation (i.e. near the instrumentation key)
  * `enableAutoRouteTracking: true // option to log all route changes`
* Possibly best placed to start in the app-start.service.ts

* Track and trace (in any place you want to track such at app.componant.ts ngoninit())
* SeverityLevel can be imported or just omit that line
   
        // Log a diagnostic scenario such entering or leaving a function
        this.appInsights.trackTrace({
            message: 'App initialised at ' + new Date().toString(),
            severityLevel: SeverityLevel.Information
        });

* Then query Application Insights Logs with the following

        traces | limit 50

![App Insights Trace Query](/Images/AppInsights_Trace_query.png)

* Custom Error Handler must be implemented to catch exceptions (so they aren't swallowed by Angular)

* [SDK Reference with valid configs](https://github.com/microsoft/ApplicationInsights-JS)


## Extracting Business Value ##

* [Continuous Export from App Insights to SQL DB](https://docs.microsoft.com/en-us/azure/azure-monitor/app/code-sample-export-sql-stream-analytics)