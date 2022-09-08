# Windows Subsystem for Linux (WSL)

WSL is a tool to run linux subsystems (e.g. VM) on a Windows machine

Microsoft provides a WSL Development Environment [Guide](https://docs.microsoft.com/en-us/windows/wsl/setup/environment?source=recommendations) for setting up a local environment

## Why?

It makes developing Linux applications from windows a breeze. Rather than working through all the setup of a VM or dual booting, WSL makes getting up an running a lot faster

The Remote Development VSCode Extension makes this even easier by connecting VSCode to a running WSL instance and allowing development of code on that Virtualized Environment.

## Useful Commands

### Get Current WSL Status

`wsl --status`

### List available Distros

`wsl --list --online`

### Install Distribution

`wsl --install -d <distro>` 
`wsl --install -d <Ubuntu>`

### See installed Distros

`wsl --list`

`wsl --list --verbose`

### Stop an Instance

Stop a single instance

`wsl --terminate <DistroName>`

Stop All Instances and WSL

`wsl --shutdown`


## Links

[Getting Started with Docker Remote Containers on WSL 2](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)

[Containers Tips and Tricks](https://code.visualstudio.com/docs/containers/troubleshooting)
