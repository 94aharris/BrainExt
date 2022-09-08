# dotnet cli useful commands

## Make the solution

- make the solution in the root

```bash
dotnet new sln
```

## Create the gitignore

```bash
dotnet new gitignore
```

## Make the project

- Create a new folder
- change directory into the new folder
- make the project

```bash
mkdir <foldername>
cd <foldername>
dotnet new console
```

- back out to the sln level
- Add project to solution

```bash
cd ..
dotnet sln add .\<foldername>
```

