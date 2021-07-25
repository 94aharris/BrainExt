# PowerShell Best Practices #

## General Best Practices ##

- Verb-Noun
- Common Verbs from `get-verb`
- Singular Noun
- `What-If`
- Outbuffer
- `Measure-command`
- Allow Empty Collection
- Test with Pester
- Make use of metadata to validate (e.g. Parameter Sets)
  - Done create code to perform actions you can get the metadata to perform. Use your time to develop code that benefits your organization
  - CmdletBinding specifies function level metadata and explicitly creates an advanced function
  - \[Paarameter\] specifies param level metadata and implicitly creates an advanced function

## Get Error Info ##

get type for catching

    $error[0].exception.getType().FullName

## Strict Script Running ##

*Best to develop scripts with strict checks on*

    set-strict -version latest

Version meanings

- 1.0
  - Prohibits references to uninitialized variables, except for uninitialized variables in strings.
- 2.0
  - Prohibits references to uninitialized variables. This includes uninitialized variables in strings.
  - Prohibits references to non-existent properties of an object.
  - Prohibits function calls that use the syntax for calling methods.
- 3.0
  - Prohibits references to uninitialized variables. This includes uninitialized variables in strings.
  - Prohibits references to non-existent properties of an object.
  - Prohibits function calls that use the syntax for calling methods.
  - Prohibit out of bounds or unresolvable array indexes.
- Latest
  - Selects the latest version available. The latest version is the most strict. Use this value to make sure that scripts use the strictest available version, even when new versions are added to PowerShell.

## Performance ##

- PowerShell is quirky If you're aware of multiple techniques to accomplish something, and you're writing a production script that will be dealing with large data sets (meaning performance will become a cumulative factor), then test the performance using Measure-Command or some other tool.

## Function Begin,Process,End ##

Functions can accept multiple values down a pipeline, begin, process, and end are used to perform function tasks.
Begin - done once before any processing on objects down the pipeline
Process - done for each of the objects pushed down the pipeline
End - done for cleanup at the end

`get-childitem | write-logstuff`

```powershell
function write-logstuff {
  param {
    # parameters here
  }
  begin {
    # do setup like making sure the output file for the log exists
  }
  process {
    # write each of the items into the log we confirmed exists
  }
  end {
    # close out the file or do final processing
  }
}
```

## Use CIM not WMI ##

- WMI is being depreciated :/  
- [WMI Depreciation](https://blog.ipswitch.com/get-ciminstance-vs-get-wmiobject-whats-the-difference)

    $vols = Get-CimInstance -ClassName Win32_Volume
    $vols[0].CimInstanceProperties | Select-Object Name,Value