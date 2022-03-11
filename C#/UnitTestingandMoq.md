# Unit Testing and Moq #

## Intro ## 

Unit testing is for wrapping tests around individual components of code (e.g. methods) to ensure
functionionality and protect against regressions

## Moq ##

Moq allows you to create implementations for Interfaces (DI) to better Unit Test

## Moq Commands ##

- .setup - Configure mock method
- .callback - take action on provided input
- .verifiable - ensure the method runs
- It.IsType\<type\> -used in .setup to specify param types

## MUnit ##

- wrap an exception up in a test
- \[ExpectedException(typeOf(exceptionType))\]

## Links ##

- [Moq Quick Start Guide](https://github.com/Moq/moq4/wiki/Quickstart)
- [Unit Testing Best Practices (Microsoft)](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)