# C\# Design Patterns #

## Data Transfer Objects (DTOs) ##

### DTO Links ###

- [Create DTOs (Microsoft)](https://docs.microsoft.com/en-us/aspnet/web-api/overview/data/using-web-api-with-entity-framework/part-5)
  
### DTO Overview ###

When a Web API exposes database entities to a client, by default a framework API directly maps to the database tables. A DTO allows you to change the 'shape of the data sent back to a client'. Useage Examples:

- **Decouple service layer from database layer**
- Remove circular references
- Hide particular properties the client should not view
- Omit some properties to reduce payload size
- Flatten object graphs that contain nested objects (for convenience)
- Avoid "over-posting" vulnerabilities
