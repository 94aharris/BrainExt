# Code Review Notes #

## Legacy Code Rewrite 4/1/2022 ##

- Use T0D0 not TODO

- You only have to abstract out the calls with DB in them
  - If they are static and don't have DB calls then they are OK
  - It's just extra work
  - make sure no DB calls in the stack, if not then leave them
  - If there's no DB call's then it's fine to leave them
  - Minimize what you have to Mock
- When abstracting the class, don't use / implement the 'facade'
  - Kill the static facade
  - Implement the interface on the actual
- Pass in the actual implementation vs a mock
- DRY and SOLID Unit Tests Mocking
  - Arrange --> Act --> Assert
  - Only one call to constructor for Class under test (e.g. build system under test private function)
  - pass in nullable mocks then true them up, only passing in ones you care about
  - Only mock dependencies that don't work in memory
  - Once you pass in the ones you care about, default the rest
  - **Use Fluent Assertions**
  - **Callbacks!**
  - Verify setups are valid and test state mutation