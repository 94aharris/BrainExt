# PowerShell Pester #

## About ##

Pester is for testing Powershell scripts

* Test files are written in form filetotest.Tests.ps1
  * Get-Stuff.Tests.Ps1
  * Catagorization works like Get-Stuff.Unit.Tests.ps1 / Get-Stuff.Acceptance.Tests.ps1
* Tests should be placed in the same directory as the files they are testing

## Setup ##

**Make Sure The File You Are dot Sourcing Contains a Function with the name you are calling...**

* Use a `BeforeAll` block to dot source the necessary files
* Use a `Describe` block to name and specify a test

```powershell
BeforeAll {
  . $PSScriptRoot/Get-DrsDisk.ps1
}
Describe 'Get-DrsDisk' {
    It "Given no parameters, it lists local disk space" {
        $diskSpace = Get-DrsDisk
        $diskSpace.count | Should -Be 2
    }
}
```

**If you are testing a module then use Import-Module .. -Force to make sure all dependencies are captured**

* Use `Context` blocks to segment different tests
  * A `BeforeAll` Block can be used within a `Context`
* Pester has it's own special foreach syntax

## Running ##

* Run with `Invoke-Pester` while in the directory of the tests (will find all *.tests.ps1 files) or explicitly specify a tests file
* See all test details with `Invoke-Pester -Output Detailed`
* See Code Coverage with `Invoke-Pester .\get-stuff.Tests.ps1 -CodeCoverage .\get-stuff.ps1`

## Mock ##

* Use `mock` to shim the data layer for running tests by overriding functions. This may not always work (see links)

```powershell
BeforeAll {
    # Import Get-STuff
    . $PSScriptRoot\Get-Stuff.ps1
    # Mock Data Layer
    Mock Get-ChildItem {
        "Hello There"
    }
}
Describe 'Get-Stuff' {
    Context "Get stuff under current dir (implements get-childitem)" {
        It "Given no parameters, it gets stuff" {
            $a = Get-Stuff
            $a | Should -Be "Hello There"
        }
    }
}
```

When using deeply linked commands try to do serialize the content out to xml using export-clixml then deserialize it back into an object to return.. [example](https://github.com/pester/Pester/issues/601)

```powershell
# Serialize the result of 'Get-Adapter' to xml
Get-Adapter | Export-Clixml -Path 'C:\tmp\adatperxml.xml'
...
# inside the test copy the contents from the xml as a string
$getAdapterMockObject = @"
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">
  <Obj RefId="0">
    <TN RefId="0">
      <T>Microsoft.Management.Infrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter</T>
      ... #etc etc
      <S N="ifDesc">Hyper-V Virtual Ethernet Adapter</S>
      <S N="ifName">ethernet_32771</S>
      <S N="DriverVersion">10.0.14393.0</S>
      <S N="LinkLayerAddress">00-15-5D-02-0F-00</S>
    </MS>
  </Obj>
</Objs>
"@

# Deserialize it back into an object
$myobj = [System.Management.Automation.PSSerializer]::Deserialize($getAdapterMockObject)

# Mock the cmdlet with the object
Mock Get-NetAdapter { return $myobj }
```

## PSDrive / Registry ##

* Pester sets up a temp drive on run, store anything here as it is cleaned up
* Pester sets up a temp registry, make any changes there


## Testing Production ##

* Pester could also be used to perform Acceptance and post deployment work in Production