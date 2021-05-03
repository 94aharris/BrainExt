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

      BeforeAll {
        . $PSScriptRoot/Get-DrsDisk.ps1
      }
      Describe 'Get-DrsDisk' {
          It "Given no parameters, it lists local disk space" {
              $diskSpace = Get-DrsDisk
              $diskSpace.count | Should -Be 2
          }
      }

* Use `Context` blocks to segment different tests
  * A `BeforeAll` Block can be used within a `Context`
* Pester has it's own special foreach syntax

## Running ##

* Run with `Invoke-Pester` while in the directory of the tests (will find all *.tests.ps1 files) or explicitly specify a tests file
* See all test details with `Invoke-Pester -Output Detailed`

## Mock ##

* Use `mock` to shim the data layer for running tests by overriding functions. This may not always work (see links)

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


## PSDrive / Registry ##
* Pester sets up a temp drive on run, store anything here as it is cleaned up
* Pester sets up a temp registry, make any changes there