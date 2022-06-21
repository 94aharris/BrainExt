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

### *Publish an Image to Azure Container Registry (ACR)*

- **Azure CLI Commands**
  - Build and run a container image w/ ACR Tasks
  - Create rg and ACR in resource group
  ```bash
  az group create --name az204-acr-rg --location <myLocation>
  
  az acr create --resource-group az204-acr-rg \
    --name <myContainerRegistry> --sku Basic
  ```
  - Create Docker file
  ```bash
  echo FROM mcr.microsoft.com/hello-world > Dockerfile
  ```
  - Build the image and push to registy
  ```bash
  az acr build --image sample/hello-world:v1  \
    --registry <myContainerRegistry> \
    --file Dockerfile .
  ```
  - List repositories in ACR
  ```bash
  az acr repository list --name <myContainerRegistry> --output table
  ```
  - List tags on the repository
  ```bash
  az acr repository show-tags --name <myContainerRegistry> \
    --repository sample/hello-world --output table
  ```
  - Run the container image
  ```bash
  az acr run --registry <myContainerRegistry> \
    --cmd '$Registry/sample/hello-world:v1' /dev/null
  ```
  - Clean up resources
  ```bash
  az group delete --name az204-acr-rg --no-wait
  ```
- Service Overview
  - Azure Container Registry Use Cases
    - Pull images from container registry to deployment targets (orchestration systems like K8s, Azure services like AKS)
    - Push to container registry as part of a container development workflow (CI)
    - Configure ACR Tasks to automatically rebuild application images. Automate building, testing, and patching images in parallel
  - **ACR Service Tiers**
    - Basic - dev / learning. Same abilities as higher tiers but lower storage and image throughput
    - Standard - Same capabilities but production level storage and image throughput
    - Premium - Highest storage and concurrent operation. Adds geo-replication, image signing, and private endpoints
  - Supported artifacts
    - read-only snapshot of Docker compatible container (Windows / Linux)
    - container rleated content (Helm charts and images to OCI Image format specification)
  - Storage Capabilities
    - Encryption-at-rest
    - Geo-Replication (Premium feature must be enabled)
    - Zone redundancy - minimum of three zones (Premium service tier) 
    - Scalable storage - many repositories, images, layers, or tags up to the registry storage limit
- ACR Tasks
  - Overview: Cloud based container image building on triggers, updates, or timers
  - Quick task
    - Build and push a single container image to a container registry without needing local Docker
    - Offload build to azure and verify automated build definitions
    ```bash
    az acr build
    ```
  - Auto Triggered Tasks
    - Build on source code update (e.g. git repo / azdo update)
    - build on base image update (e.g. public repo image Docker Hub update)
    - build on schedule (e.g. running workloads, maintenance, or tests on images)
    ```bash
    az acr task create
    ```
  - Multi-stp task
    - extended capability with multi-step, multi-container based workflows
    - YAML file based
    - define execution (e.g. build the web app image -> run web app container -> build test image -> run test container -> if tests pass build help chart)
- Docker File
  - Base image, commands to update base OS, build artifacts, services to expose, command to run when launched
  - example ASP .NET Core website
  ```bash
  # Step 1: Specify the parent image for the new image
  FROM ubuntu:18.04

  # Step 2: Update OS packages and install additional software
  RUN apt -y update &&  apt install -y wget nginx software-properties-common apt-transport-https \
    && wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && add-apt-repository universe \
    && apt -y update \
    && apt install -y dotnet-sdk-3.0

  # Step 3: Configure Nginx environment
  CMD service nginx start

  # Step 4: Configure Nginx environment
  COPY ./default /etc/nginx/sites-available/default

  # STEP 5: Configure work directory
  WORKDIR /app

  # STEP 6: Copy website code to container
  COPY ./website/. .

  # STEP 7: Configure network requirements
  EXPOSE 80:8080

  # STEP 8: Define the entry point of the process that runs in the container
  ENTRYPOINT ["dotnet", "website.dll"]
  ```
### *Run Containers by Using Azure Container Instance*

