 # PowerShell Best Practices #

 ## General Best Practices ##
 * Verb-Noun
 * Common Verbs from `get-verb`
 * Singular Noun
 * `What-If`
 * Outbuffer
 * `Measure-command`
 * Allow Empty Collection


## Get Error Info ##

get type for catching

    $error[0].exception.getType().FullName


## Strict Script Running ##

*Best to develop scripts with strict checks on*

    set-strict -version latest

Version meanings

* 1.0
  * Prohibits references to uninitialized variables, except for uninitialized variables in strings.
* 2.0
  * Prohibits references to uninitialized variables. This includes uninitialized variables in strings.
  * Prohibits references to non-existent properties of an object.
  * Prohibits function calls that use the syntax for calling methods.
* 3.0
  * Prohibits references to uninitialized variables. This includes uninitialized variables in strings.
  * Prohibits references to non-existent properties of an object.
  * Prohibits function calls that use the syntax for calling methods.
  * Prohibit out of bounds or unresolvable array indexes.
* Latest
  * Selects the latest version available. The latest version is the most strict. Use this value to make sure that scripts use the strictest available version, even when new versions are added to PowerShell.