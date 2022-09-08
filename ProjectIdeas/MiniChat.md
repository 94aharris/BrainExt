# MiniChat

Mini dotnet chat application running in a docker container on WSL.

Uses Cassandra for persistence and a Redis Cache (also containers)

## Setup

TinyChat
|_ tinychat.sln
|_ \API
|__ api.csproj
|_ \Core
|__ core.csproj
|_ \Infrastructure
|__ infrastructure.csproj

commands ran

```PowerShell
mkdir .\TinyChat
cd TinyChat
dotnet new sln
dotnet new gitignore
mkdir .\api
cd api
dotnet new webapi
cd ..
mkdir .\core
cd ..
cd core
dotnet new classlib
mkdir .\infrastructure
cd ..
cd infrastructure
dotnet new classlib
cd ..
dotnet sln add \api\
dotnet sln add \core\
dotnet sln add \infrastructure\
mkdir tests
cd .\tests\
mkdir coreTests
mkdir infrastructureTests
mkdir apiTests
cd .\apiTests\
dotnet new mstest
cd ..
cd .\coreTests\
dotnet new mstest
cd ..
cd .\infrastructureTests\
dotnet new mstest
dotnet sln add .\tests\apiTests\apiTests.csproj
dotnet sln add .\tests\coreTests\coreTests.csproj
dotnet sln add .\tests\infrastructureTests\infrastructureTests.csproj
dotnet add .\api\api.csproj reference .\infrastructure\infrastructure.csproj
dotnet add .\api\api.csproj reference .\core\core.csproj
dotnet add .\infrastructure\infrastructure.csproj reference .\core\core.csproj
dotnet build
```