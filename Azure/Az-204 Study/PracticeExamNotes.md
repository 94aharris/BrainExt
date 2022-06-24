# Practice Exam Notes

## 6/23 Practice

- Connection Strings for Azure Service Bus
  - Use managed Identity to establish password less authentication
  - AMQP (Advanced Message Queueing Protocol) is the most efficient way to connect to a service bus
-  Custom handlers
  - Designed to fit the situation for developers to implement a function app in a language currently not supported
  - Only requirement for Custom hanler is that the web server has to be restarted within 60 seconds
  - Application setting "FUNCTIONS_WORKER_RUNTIME":"Custom"
- Application Insights
  - Connect to App Insights with Instrumentation Key
- Azure Durable Functions
  - Fan-out/Fan-In allows for execution of multiple functions in parallel and wait for all to finish
- Azure Autoscaling
  - Autoscaling is handled by Azure Monitor 
  - az monitor autoscale rule create -g <resource_group> --resource <webappname> --autoscale-name <monitorscalename> --scale <in/out> --condition
- Azure Functions Timing
  - [Reference doc](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=in-process&pivots=programming-language-csharp#ncrontab-expressions)
  - 0 0 0 1-7 * 1 == First Monday of every month
- Azure Durable Functions
  - ListInstancesAsync() - get the statuses of all orchestration instances
  - PurgeInstanceHistoryAsync() - delete any Azure Table rows and large message blobs associated with a completed instance
- Remote Desktop to Linux VM 
  - [Reference Document](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop)
  - Open RDP port 3389
  - Install xfce (lightweight desktop environment)
  - Install xrdp (remote desktop service)
  
  
