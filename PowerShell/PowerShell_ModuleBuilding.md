# PowerShell Module Building #

## Directory Setup ##

    ProjectRoot
    -DoStuffPro
    --Private
    ---format-stuff.ps1
    ---calculate-stuff.ps1
    --Public
    ---Get-Stuff.ps1
    ---Set-Stuff.ps1
    --DoStuffPro.psd1
    --DoStuffPro.psm1
    -Tests
    --Get-Stuff.Tests.ps1
    --Set-Stuff.Tests.ps1
    -README.MD

*  Under the root folder setup the following folders
   *  Project Name folder - for the contents
   *  Tests - for the pester tests
   *  README.md - for the info about the project
*  Under the Project Name Folder setup the following folders
   *  Public - For the functions to make visible
   *  Private - For the functions to use internally
   *  projectname.psd1 - Manifest file to use for import
   *  projectname.psm1 - Defines how to handle imports


## Simple .psm1 Example ##
*Simple Example of the .psm1*
    
      
    #Get public and private function definition files.
        $Public  = @( Get-ChildItem -Path $PSScriptRoot\Public\*.ps1 -ErrorAction SilentlyContinue )
        $Private = @( Get-ChildItem -Path $PSScriptRoot\Private\*.ps1 -ErrorAction SilentlyContinue )

    #Dot source the files
        Foreach($import in @($Public + $Private))
        {
            Try
            {
                . $import.fullname
            }
            Catch
            {
                Write-Error -Message "Failed to import function $($import.fullname): $_"
            }
        }

    # Here I might...
        # Read in or create an initial config file and variable
        # Export Public functions ($Public.BaseName) for WIP modules
        # Set variables visible to the module and its functions only

    Export-ModuleMember -Function $Public.Basename

## Manifest (.psd1) File ##

* These are a bit more complicated but can generally be created with a template
* Make sure the .psm1 is referenced
* [Good Example](https://github.com/RamblingCookieMonster/PSStackExchange/blob/db1277453374cb16684b35cf93a8f5c97288c41f/PSStackExchange/PSStackExchange.psd1)

## How to Do an Import ##

* For a simple module like this just Import the .psd1
* `Import-Module .\projectname.psd1`