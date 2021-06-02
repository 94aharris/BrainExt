# PowerShell ToolMaking #

## Tips ##
* Remember Single Responsibility Principal
  * Make use of the pipeline
  * You do not have Get-Service -Format HTML you have Get-Service | ConvertTo-Html
  * Your functions shouldn't handle for everything
  * Remember how a pipeline behaves

![PowerShell Pipeline](../Images/blocksPipeline.svg)

## Best Practices Style Guide ##
* [MS Encouraged Parameter Names](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/standard-cmdlet-parameter-names-and-types?view=powershell-7.1)
* [MS Strongly Encouraged Guidelines](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/strongly-encouraged-development-guidelines?view=powershell-5.1)
* [Posh Powershell Style Guide](https://poshcode.gitbook.io/powershell-practice-and-style/)
* [PowerShell Gallery Publishing Guidelines](https://docs.microsoft.com/en-us/powershell/scripting/gallery/concepts/publishing-guidelines?view=powershell-7.1)
* [MS PowerShell Docs Style Guide](https://docs.microsoft.com/en-us/powershell/scripting/community/contributing/powershell-style-guide?view=powershell-7.1)