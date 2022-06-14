# General C\# Notes #

## Terms ##

- JFDI - Just Fkn Do It
  
## Static Classes / Methods ##

- Static class variables are not thread safe
- Static methods cannot be methods that extend an interface

## Refactoring ##

- The IOC pattern
  - Find 'new'
  - Go to definition
  - Right Click Class
  - De-Static
  - Extract Interface
  - Fix everywhere
  - Test it up

## Types ##

### var ###

### type? ###

question mark means nullable

## Helpful Methods ##

- TypeOf()
  - Get the type of a class

## Doing tasks in the background ##

### Async / Await ###

[dotnet AsyncOperation Class](https://docs.microsoft.com/en-us/dotnet/api/system.componentmodel.asyncoperation?view=net-6.0)
[dotnet Asynchronous Programming Pattern: Event-Based Asynchronous Pattern](https://docs.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/event-based-asynchronous-pattern-overview)

- syntax for asynchronously awaiting on asynchronous operations. these operations may or may not use a thread pool

### BackgroundWorker ###

[dotnet BackgroundWorker Class](https://docs.microsoft.com/en-us/dotnet/api/system.componentmodel.backgroundworker?view=net-6.0)

- model a single task that you want to perform in the background on a thread pool thread
- Allows you to run an operation on a separate dedicated thread. Time-consuming operations (e.g. downloads and database transactions) can make the UI
seem like it stopped working. When you want a responsive UI as you are faced with operation delays, use the BackgroundWorker class.

## Architecture ##

### Dependency Injection ###

[dotnet Dependency Injection Overview](https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection)
[Simple Injector DI Quickstart](https://docs.simpleinjector.org/en/latest/quickstart.html#a-quick-example)
[Dependency Injection Practice, Principles, and Patterns (book)](https://www.manning.com/books/dependency-injection-principles-practices-patterns?utm_source=DNJ&utm_medium=affiliate&utm_campaign=book_seemann2_dependency_3_4_19&a_aid=DNJ&a_bid=844515ef)

### Command and Query Responsibility Segregation (CQRS) ###

[CQRS Pattern (MS Architecture)](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs#:~:text=CQRS%20stands%20for%20Command%20and,operations%20for%20a%20data%20store.)

- An architecture pattern that is often used in event driven applications and frequently associated with event sourcing.
- separates read and update operations for a data store

### Model View Controller (MVC) ###

- Model = set of classes representing data the app manages

### Entity Framework ###

### Architecture Resources ###

[Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/)