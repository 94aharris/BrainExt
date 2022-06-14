# Simple Injector #

## Overview ##

- Main type Container class is used to register mappings between each abstration (service) and it's implementation (component)
- Container is like a dictionary where the abstraction is the key and each related value is the definition
- Use one Container. instances are thread safe. Creating the container has large overhead, accessing an instance is fast.
- Six steps for use

1. Create a new Container (new)
2. Configure the container (Register)
3. Verify the container (Verify)
4. Store the container for use by the application ()
5. Retrieve instances from the container (Resolve)
6. Dispose of the container instance when application ends (optional)

## Constructors ##

Simple Injector disallows Auto-wiring constructors that contain primitive types. The below will throw an error on container validation.

```C#
// THIS IS BAD
public class SqlUserRepository : IUserRepository
{
    private readonly IUserContext userContext;
    private readonly string connectionString;

    // This constructors contains a 'real' dependency and a primitive type.
    public UserController(IUserContext userContext, string connectionString)
    {
        this.userContext = userContext;
        this.connectionString = connectionString;
    }
}

```

Solution is to wrap all the type's primitive constructor arguments in a new type, even if that means wrapping a single value.

```C#
// THIS IS GOOD

// New class that wraps the connection string.
public class SqlUserRepositorySettings
{
    public SqlUserRepositorySettings(string connectionString) =>
        this.ConnectionString = connectionString;

    public string ConnectionString { get; }
}

public class SqlUserRepository : IUserRepository
{
    private readonly IUserContext userContext;
    private readonly SqlUserRepositorySettings settings;

    // Depend on the new wrapper type instead
    public UserController(
        IUserContext userContext, SqlUserRepositorySettings settings)
    {
        this.userContext = userContext;
        this.settings = settings;
    }
}
```

## Resources ##

- [Simple Injector DI Quickstart](https://docs.simpleinjector.org/en/latest/quickstart.html#a-quick-example)