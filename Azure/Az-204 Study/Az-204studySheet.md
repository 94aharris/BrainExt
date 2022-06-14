# AZ-204

## 1.1 Implement IaaS Solutions

### *Provision Virtual Machines (VMs)*

- **CLI Commands**
  - Az CLI VM Image List

    ```bash
    az vm image list
    ```
  - Create Resource Group
    ```bash
    az group create --name <rg-name> --location <location>
    ```
  - Create VM
    ```bash
    az vm create \
    --resource-group <rg-name> \
    --name <vm-name> \
    --image <image-name> \
    --generate-ssh-keys \
    --admin-username <username>
    ```
  - Open Port
    ```bash
    az vm open-port --port <port> \
    --resource-group <rg-name>
    --name <vm-name>
    ```
  - Connect to VM
   ```bash
   ssh azureuser@<publicIPAddress> 
   ```
  - Update VM and Install nginx
   ```bash
   sudo apt-get -y update
   sudo apt-get -y install nginx
   ```
  - Delete azure resource group
   ```bash
   az group delete --name az204-vm-rg --no-wait
   ```
- Helpful extensions
  - Custom script extention - scripts after the fact
  - DSC - deploy dsc configs
  - Diagnostics Extension - collect diagnostics
- Fault Tolerance
  - Availability Zones - Fault Domain + Update Domain
  - Availability Set - logical grouping of VMs to allow Azure to balance accross update and fault domains
  - Fault Domain - Hardware / Power Boundary
  - Update Domain - Hardware that may be rebooted at the same time
- Security Tips
  - Do not configure a VM for remote access from public IP, use vnet

### *Configure, Validate, and Deploy ARM Templates*

- **CLI & PowerShell Commands**
  - set deployment mode w/ powershell
  ```powershell
  New-AzResourceGroupDeployment `
  -Mode Complete `
  -Name ExampleDeployment `
  -ResourceGroupName ExampleResourceGroup `
  -TemplateFile c:\MyTemplates\storage.json
  ```
  - set deployment mode with cli
  ```bash
  az deployment group create \
  --mode Complete \
  --name ExampleDeployment \
  --resource-group ExampleResourceGroup \
  --template-file storage.json
  ```
  - connect to azure
  ```bash
  az login
  ```
  - create resource group
  ```bash
  az group create --name <rg-name> --location <location>
  ```
  - Deploy ARM template
  ```bash
  az deployment group create --resource-group <rg-name> --template-file <template.json> --parameters <template.parameters.json>
  ```
  - Show storage account (validate)
  ```bash
  az storage account show --resource-group <rg-name> --name <storage-acct-name>
- ARM Templates Overview
  - Declarative (Make it so)
  - Idempotent
  - File
    - Parameters
    - Variables
    - Functions
    - Resources
    - Outputs
  - Ways to deploy
    - Portal
    - CLI
    - PowerShell
    - REST API
    - Github Button
    - Azure Cloud Shell
  - Terms to remember
    - *condition* - specify whether the resource is deployed only if condition is true
    - *depends on* - separate artifact must be deployed first, different than Parent/ Child 
  - Deployment Modes
    - Complete - makes it exact, deletes things that are not in the template
    - Incremental - leaves unchanged resources, only adds new

### *Configure Container Images for Solutions*

### *Publish an Image to Azure Container Registry*

### *Run Containers by Using Azure Container Instance*

