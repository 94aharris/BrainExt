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

## First run fun

- in the api project, modify the launchSettings.json to remove the SSL ports and HTTPS to focus on the app portion rather than the ssl.
- ctrl+F5 to run the app
- <localhost:port>/swagger/index.html

## CI/CD

### Build
- Setup new AzureDevOps Project
- Create New Pipeline
  - Source repository is github
- Configure Laptop as Build Agent
 - [Configure Self Hosted Agent](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/v2-windows?view=azure-devops)
 - Create Agent Running Folder
 - Download Agent
 - Generate Personal Access Token
 - auth
 - Run interactively not as a service
 - `.\run.cmd` accepts jobs interactively
 - `.\run.cmd` accepts only one job (useful for docker / ACI)
- Run Build agent

```PowerShell
cd d:\agent\
.\run.cmd
```

- Worked on Build YAML
- Setup Azure Cloud Shell
  - authenticate
  - create cloud shell storage
  - [DevOps CLI](https://docs.microsoft.com/en-us/azure/devops/cli/?view=azure-devops)
- Execute Pipeline
    - Build failed on local, missing requirements (visual studio, mstest, ..)
    - Changed pipeline yaml to build on cloud build box
    - Modify Pipeline YAML to use dotnetcli instead of VSBuild / VSTest (**can prob build local now**)
    - Build Test and Deploy .Net Core Apps via Pipeline [MS Doc](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops&tabs=dotnetfive)
    - Success!

### Release

- Create container registry
- Create app service
- Setup Release Pipeline

### Test

