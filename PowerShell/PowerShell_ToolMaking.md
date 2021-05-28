# PowerShell ToolMaking #

## Tips ##
* Remember Single Responsibility Principal
  * Make use of the pipeline
  * You do not have Get-Service -Format HTML you have Get-Service | ConvertTo-Html
  * Your functions shouldn't handle for everything
  * Remember how a pipeline behaves

![PowerShell Pipeline](../Images/blocksPipeline.svg)