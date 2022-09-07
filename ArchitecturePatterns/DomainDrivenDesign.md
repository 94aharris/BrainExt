# Domain Driven Design

## Overview

Design application to align with Business Truths rather than to align with a databse schema. Use concrete project references (disallowing circular dependencies) to add constraints forcing you to follow DI.

## Key Projects

- Application/API
  - Reference Core and Infrastructure
  - Use Repository Interfaces/Contracts
- Core/Domain/Model 
  - No Dependencies to Other Layers
  - Implements Repository Contracts/Interfaces to be used in DI
- Infrastructure
  - Reference Core
  - Direct dependency on infrastructure framework like EF or other DB

![](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/media/ddd-oriented-microservice/domain-driven-design-microservice.png)