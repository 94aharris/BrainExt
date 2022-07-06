# AZ-204

- [AZ-204](#az-204)
  - [0.0 Resources](#00-resources)
  - [1 - Develop Azure Compute Solutions (25-30%)](#1---develop-azure-compute-solutions-25-30)
  - [1.1 Implement IaaS Solutions](#11-implement-iaas-solutions)
    - [*Provision Virtual Machines (VMs)*](#provision-virtual-machines-vms)
      - [**CLI Commands** - Provision VMs](#cli-commands---provision-vms)
      - [Helpful extensions](#helpful-extensions)
      - [Fault Tolerance](#fault-tolerance)
      - [Resources - Azure VM](#resources---azure-vm)
    - [*Configure, Validate, and Deploy ARM Templates*](#configure-validate-and-deploy-arm-templates)
      - [**CLI & PowerShell Commands** - ARM Templates](#cli--powershell-commands---arm-templates)
      - [ARM Templates Overview](#arm-templates-overview)
      - [Ways to Deploy ARM](#ways-to-deploy-arm)
      - [ARM Terms to remember](#arm-terms-to-remember)
      - [Resources ARM Templates](#resources-arm-templates)
    - [*Configure Container Images for Solutions*](#configure-container-images-for-solutions)
      - [**CLI Commands** - Configure Container Images](#cli-commands---configure-container-images)
      - [**Important Tips** - Container Images](#important-tips---container-images)
      - [Overview - Container Images](#overview---container-images)
      - [High Level Process for Creating Container Image](#high-level-process-for-creating-container-image)
    - [*Publish an Image to Azure Container Registry (ACR)*](#publish-an-image-to-azure-container-registry-acr)
      - [**CLI Commands** - Publish Image to ACR](#cli-commands---publish-image-to-acr)
    - [Overview - ACR](#overview---acr)
      - [**ACR Service Tiers**](#acr-service-tiers)
      - [ACR Supported artifacts](#acr-supported-artifacts)
      - [Storage Capabilities](#storage-capabilities)
      - [ACR Authentication](#acr-authentication)
      - [ACR Tasks](#acr-tasks)
      - [ACR Docker File](#acr-docker-file)
    - [*Run Containers by Using Azure Container Instance*](#run-containers-by-using-azure-container-instance)
      - [**CLI Commands** - Run Container Instance](#cli-commands---run-container-instance)
      - [**Things to remember** - Container Instances](#things-to-remember---container-instances)
      - [Containerized Tasks Restart Policies](#containerized-tasks-restart-policies)
      - [Container Instances Environmental variables](#container-instances-environmental-variables)
      - [Mount Azure file share in Azure Container Instances (ACI)](#mount-azure-file-share-in-azure-container-instances-aci)
  - [1.2 Create Azure App Service Web Apps](#12-create-azure-app-service-web-apps)
    - [*Create an Azure App Service Web App*](#create-an-azure-app-service-web-app)
      - [**CLI Commands** - Create App Service Web App](#cli-commands---create-app-service-web-app)
      - [**Important Notes** - App Service Web App](#important-notes---app-service-web-app)
      - [Overview - Create App Service Web App](#overview---create-app-service-web-app)
      - [App Service Plans](#app-service-plans)
      - [Running and Scaling App Service](#running-and-scaling-app-service)
      - [App Service Web App Deployment](#app-service-web-app-deployment)
      - [App Service Web App Authentication](#app-service-web-app-authentication)
      - [App Service Networking Features](#app-service-networking-features)
      - [Resources - Create Azure App Service](#resources---create-azure-app-service)
    - [*Enable Diagnostics Logging*](#enable-diagnostics-logging)
      - [**CLI Commands**](#cli-commands)
      - [Overview - Web App Diagnostics](#overview---web-app-diagnostics)
      - [Available Logging by Framework](#available-logging-by-framework)
      - [Alternatives](#alternatives)
      - [Live Log Streaming](#live-log-streaming)
      - [Enable Logging (Portal)](#enable-logging-portal)
      - [Resources](#resources)
    - [*Deploy Code to a Web App*](#deploy-code-to-a-web-app)
      - [**CLI Commands** - Deploy Web App](#cli-commands---deploy-web-app)
      - [Tips to Remember - Deploy Code to a Web App](#tips-to-remember---deploy-code-to-a-web-app)
      - [Overview - Deploy Code to a Web App](#overview---deploy-code-to-a-web-app)
      - [Azure DevOps Pipelines](#azure-devops-pipelines)
      - [Using Deployment Slots](#using-deployment-slots)
      - [Resources - Deploy Code to a Web App](#resources---deploy-code-to-a-web-app)
    - [*Configure Web App Settings Including SSL, API Settings, and Connection Strings*](#configure-web-app-settings-including-ssl-api-settings-and-connection-strings)
      - [*CLI Commands* - Configure Web App Settings](#cli-commands---configure-web-app-settings)
      - [Web App Settings Overview](#web-app-settings-overview)
      - [General Web App Settings](#general-web-app-settings)
      - [Web App Path Mappings](#web-app-path-mappings)
      - [Configure Web App Security Certificates](#configure-web-app-security-certificates)
      - [Configure App Features (Feature Flags)](#configure-app-features-feature-flags)
      - [Resources - Configure Web App Settings](#resources---configure-web-app-settings)
    - [*Implement Autoscaling Rules Including Scheduled Autoscaling and Autoscaling by Operational or System Metrics*](#implement-autoscaling-rules-including-scheduled-autoscaling-and-autoscaling-by-operational-or-system-metrics)
      - [**CLI Commands** Autoscaling](#cli-commands-autoscaling)
      - [Autoscaling Tips to Remember](#autoscaling-tips-to-remember)
      - [Overview - Implement Autoscaling](#overview---implement-autoscaling)
      - [Conditions, Metrics, and Actions for autoscale rules](#conditions-metrics-and-actions-for-autoscale-rules)
      - [Enable App Service Autoscaling](#enable-app-service-autoscaling)
    - [Autoscale best practices](#autoscale-best-practices)
      - [Resources - Azure Autoscaling](#resources---azure-autoscaling)
  - [1.3 Implement Azure Functions](#13-implement-azure-functions)
    - [*Create and Deploy Azure Function Apps*](#create-and-deploy-azure-function-apps)
      - [Overview - Azure Functions](#overview---azure-functions)
      - [Azure Functions Plans](#azure-functions-plans)
      - [Azure Functions Development](#azure-functions-development)
      - [Scale Azure Functions](#scale-azure-functions)
      - [Resources - Deploy Azure Function Apps](#resources---deploy-azure-function-apps)
    - [*Implement Input and Output Bindings for a Function*](#implement-input-and-output-bindings-for-a-function)
      - [Overview Input and Output Bindings](#overview-input-and-output-bindings)
      - [Create Triggers and Bindings](#create-triggers-and-bindings)
      - [Connection Azure Functions to Azure Services](#connection-azure-functions-to-azure-services)
      - [Resources - IO Bindings for a Function](#resources---io-bindings-for-a-function)
    - [*Implement Function Triggers by Using Data Operations, Timers, and Webhooks*](#implement-function-triggers-by-using-data-operations-timers-and-webhooks)
      - [Overview - Azure Function Triggers](#overview---azure-function-triggers)
      - [Trigger Azure Function on Timer](#trigger-azure-function-on-timer)
      - [Trigger Azure Functions with HTTP Request](#trigger-azure-functions-with-http-request)
      - [Trigger Azure Function with Data Operation](#trigger-azure-function-with-data-operation)
      - [Trigger Azure Function with Webhook](#trigger-azure-function-with-webhook)
      - [Resources - Azure Function Triggers](#resources---azure-function-triggers)
    - [*Implement Azure Durable Functions*](#implement-azure-durable-functions)
      - [Overview - Durable Functions](#overview---durable-functions)
      - [Durable Function Application Patterns](#durable-function-application-patterns)
      - [Four Function Types](#four-function-types)
      - [Task Hubs](#task-hubs)
      - [Resources - Azure Durable Functions](#resources---azure-durable-functions)
  - [2 Develop for Azure Storage (15-20%)](#2-develop-for-azure-storage-15-20)
  - [2.1 Develop Solutions that Use Cosmos DB Storage](#21-develop-solutions-that-use-cosmos-db-storage)
    - [*Select the Appropriate API and SDK for a Solution*](#select-the-appropriate-api-and-sdk-for-a-solution)
    - [*Implement Partitioning Schemes and Partition Keys*](#implement-partitioning-schemes-and-partition-keys)
    - [*Perform Operations on Data and Cosmos DB Containers*](#perform-operations-on-data-and-cosmos-db-containers)
      - [Resources - Perform Operations on Cosmos DB](#resources---perform-operations-on-cosmos-db)
    - [*Set the Appropriate Consistency Level for Operations*](#set-the-appropriate-consistency-level-for-operations)
    - [*Manage Change Feed Notifications*](#manage-change-feed-notifications)
  - [2.2 Develop Solutions thatUse Blob Storage](#22-develop-solutions-thatuse-blob-storage)
    - [*Move Items in Blob Storage Between Storage Accounts or Containers*](#move-items-in-blob-storage-between-storage-accounts-or-containers)
    - [*Set and Retrieve Properties and Metadata*](#set-and-retrieve-properties-and-metadata)
    - [*Perform Operations on Data by Using the Appropriate SDK*](#perform-operations-on-data-by-using-the-appropriate-sdk)
    - [*Implement Storage Policies, Data Archiving, and Retention*](#implement-storage-policies-data-archiving-and-retention)
  - [3 Implement Azure Security (20-25%)](#3-implement-azure-security-20-25)
  - [3.1 Implement user authentication and authorization](#31-implement-user-authentication-and-authorization)
    - [*Authenticate and Authorize Users by using the Microsoft Identity Platform*](#authenticate-and-authorize-users-by-using-the-microsoft-identity-platform)
    - [*Authenticate and Authorize Users and Apps by using Azure Active Directory*](#authenticate-and-authorize-users-and-apps-by-using-azure-active-directory)
    - [*Create and Implement Shared Access Signatures*](#create-and-implement-shared-access-signatures)
    - [*Implement Solutions with Microsoft Graph*](#implement-solutions-with-microsoft-graph)
  - [3.2 Implement secure cloud solutions](#32-implement-secure-cloud-solutions)
    - [*Secure App Configuration Data by Using App Configuration or Azure Key Vault*](#secure-app-configuration-data-by-using-app-configuration-or-azure-key-vault)
    - [*Develop Code that Uses Keys, Secrets, and Certificates Stored in Azure Key Vault*](#develop-code-that-uses-keys-secrets-and-certificates-stored-in-azure-key-vault)
    - [*Implement Managed Identities for Azure Resources*](#implement-managed-identities-for-azure-resources)
  - [4 Monitor, troubleshoot, and optimize Azure solutions (15-20%)](#4-monitor-troubleshoot-and-optimize-azure-solutions-15-20)
  - [4.1 Implement caching for solutions](#41-implement-caching-for-solutions)
    - [*configure cache and expiration policies for Azure Cache for Redis*](#configure-cache-and-expiration-policies-for-azure-cache-for-redis)
    - [*implement secure and optimized application cache patterns including data sizing, connections, encryption, and expiration*](#implement-secure-and-optimized-application-cache-patterns-including-data-sizing-connections-encryption-and-expiration)
  - [4.2 Troubleshoot solutions by using metrics and log data](#42-troubleshoot-solutions-by-using-metrics-and-log-data)
    - [*configure an app or service to use Application Insights*](#configure-an-app-or-service-to-use-application-insights)
    - [*review and analyze metrics and log data*](#review-and-analyze-metrics-and-log-data)
    - [*implement Application Insights web tests and alerts*](#implement-application-insights-web-tests-and-alerts)
  - [5 Connect to and consume Azure services and third-party services (15-20%)](#5-connect-to-and-consume-azure-services-and-third-party-services-15-20)
    - [5.1 Implement API Management](#51-implement-api-management)
    - [*create an APIM instance*](#create-an-apim-instance)
    - [*create and document APIs*](#create-and-document-apis)
    - [*configure authentication for APIs*](#configure-authentication-for-apis)
    - [*define policies for APIs*](#define-policies-for-apis)
    - [5.2 Develop event-based solutions](#52-develop-event-based-solutions)
    - [*implement solutions that use Azure Event Grid*](#implement-solutions-that-use-azure-event-grid)
    - [*implement solutions that use Azure Event Hub*](#implement-solutions-that-use-azure-event-hub)
    - [5.3 Develop message-based solutions](#53-develop-message-based-solutions)
    - [*implement solutions that use Azure Service Bus*](#implement-solutions-that-use-azure-service-bus)
    - [*implement solutions that use Azure Queue Storage queues*](#implement-solutions-that-use-azure-queue-storage-queues)

## 0.0 Resources

- [AZ-204 Exam Information](https://docs.microsoft.com/en-us/learn/certifications/exams/az-204)
- [Thomas Maurer AZ-204 Study Guide](https://www.thomasmaurer.ch/2020/03/az-204-study-guide-developing-solutions-for-microsoft-azure/)
- [Whizlabs AZ-204 Practice Exam](https://www.whizlabs.com/microsoft-azure-certification-az-204/)
- [Create Serverless Applications (MS Learning Path)](https://docs.microsoft.com/en-us/learn/paths/create-serverless-applications/)

## 1 - Develop Azure Compute Solutions (25-30%)

## 1.1 Implement IaaS Solutions

### *Provision Virtual Machines (VMs)*

#### **CLI Commands** - Provision VMs

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

#### Helpful extensions

- Custom script extention - scripts after the fact
- DSC - deploy dsc configs
- Diagnostics Extension - collect diagnostics

#### Fault Tolerance

- Availability Zones - Fault Domain + Update Domain
- Availability Set - logical grouping of VMs to allow Azure to balance accross update and fault domains
- Fault Domain - Hardware / Power Boundary
- Update Domain - Hardware that may be rebooted at the same time

#### Resources - Azure VM

- [Quickstart: Create a Windows virtual machine in the Azure portal](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal)
- [Tutorial: Create and Manage Windows VMs with Azure PowerShell](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/tutorial-manage-vm)
- [How to connect and sign on to an Azure virtual machine running Windows](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/connect-logon)
- [Quick steps: Create and use an SSH public-private key pair for Linux VMs in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/mac-create-ssh-keys)

### *Configure, Validate, and Deploy ARM Templates*

#### **CLI & PowerShell Commands** - ARM Templates

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
```

#### ARM Templates Overview

- Declarative (Make it so)
- Idempotent
- File
  - Parameters
  - Variables
  - Functions
  - Resources
  - Outputs

#### Ways to Deploy ARM

- Portal
- CLI
- PowerShell
- REST API
- Github Button
- Azure Cloud Shell
- Deployment Modes
  - Complete - makes it exact, deletes things that are not in the template
  - Incremental - leaves unchanged resources, only adds new

#### ARM Terms to remember
  
- *condition* - specify whether the resource is deployed only if condition is true
- *depends on* - separate artifact must be deployed first, different than Parent/ Child

#### Resources ARM Templates

- [Extend ARM templates by using deployment scripts](https://docs.microsoft.com/en-us/learn/modules/extend-resource-manager-template-deployment-scripts/)
- [Advanced Azure Resource Manager template functionality](https://docs.microsoft.com/azure/architecture/guide/azure-resource-manager/advanced-templates/)
- [Azure Resource Manager templates overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)
- [Tutorial: Create and deploy your first Azure Resource Manager template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template)

### *Configure Container Images for Solutions*

#### **CLI Commands** - Configure Container Images

- clone sample app repo

```bash
git clone https://github.com/Azure-Samples/aci-helloworld.git
```

- Specify container with dockerfile

```dockerfile
FROM node:8.9.3-alpine
RUN mkdir -p /usr/src/app
COPY ./app/* /usr/src/app/
WORKDIR /usr/src/app
RUN npm install
CMD node /usr/src/app/index.js
```

- Build container with docker

```bash
docker build ./aci-helloworld -t aci-tutorial-app
```

- See built images

```bash
docker images
```

- run container locally

```bash
docker run -d 8080:80 aci-tutorial-app
```

- Create resource group and container registry

```bash
az group create --name myResourceGroup --location eastus

az acr create --resource-group myResourceGroup --name <acrName> --sku Basic
```

- Log into container registry

```bash
az acr login --name <acrName>
```

- Tag container image
  - To push a container image to a private registry you must tag the image with the full name of the registry's login server

  ```bash
  az acr show --name <acrName> --query loginServer --output table
  ```

  - display list of local images

  ```bash
  docker images
  ```

  - tag image with the login server of container registry and add :v1 to indicate image version

  ```bash
  docker tag aci-tutorial-app <acrLoginServer>/aci-tutorial-app:v1
  ```

  - verify tagging

  ```bash
  docker images
  ```

  - Push image to Azure Container Registry

  ```bash
  docker push <acrLoginServer>/aci-tutorial-app:v1
  ```

  - List images in Azure Container Registry

  ```bash
  az acr repository list --name <acrName> --output table
  ```

  - view tags for specific image

  ```bash
  az acr repository show-tags --name <acrName> --repository aci-tutorial-app
  ```

- Deploy the Container
  - Get registry credentials, best practice is to create and configure Azure Active Directory service principal with pull permissions to the registry
  - Get login server

  ```bash
  az acr show --name <acrName> --query loginServer
  ```

  - Deploy Container with credentials (dns-name-label must be unique within Azure region)

  ```bash
  az container create \
    --resource-group myResourceGroup \
    --name aci-tutorial-app \
    --image <acrLoginServer>/aci-tutorial-app:v1 \
    --cpu 1 --memory 1 \
    --registry-login-server <acrLoginServer> \
    --registry-username <service-principal-ID> \
    --registry-password <service-principal-password> \
    --ip-address Public --dns-name-label <aciDnsLabel> --ports 80 
  ```

  - Verify deployment progress

  ```bash
  az container show --resource-group myResourceGroup --name aci-tutorial-app --query instanceView.state
  ```

- view application and container logs
  - Display container FQDN

  ```bash
  az container show --resource-group myResourceGroup --name aci-tutorial-app --query ipAddress.fqdn
  ```

  - Display container IP address

  ```bash
  az container show --resource-group myResourceGroup --name aci-tutorial-app --query ipAddress.ip --output table
  ```

  - View log output

  ```bash
  az container logs --resource-group myResourceGroup --name aci-tutorial-app 
  ```

- Replicate a container image to different azure regions
  - Replicate to another region

  ```bash
  az acr replication create --registry <acr_name> --location japaneast
  ```

  - Retrieve all container image replicas

  ```bash
  az acr replication list --registry <acr_name> --output table
  ```

- Clean-up

```bash
az group delete --name myResourceGroup
```

- Enable Registry Admin account (EXPLORATION ONLY)

```bash
az acr update --name <acr_Name> --admin-enabled true
```

- Retrieve username and password for admin account

```bash
az acr credential show --name <acr_name>
```

#### **Important Tips** - Container Images

- ACR is a private registry. Images cannot be accessed without authentication
- Azure service principals are the recommended authentication method. They provide granular access to container images in ACR
- When geo-replicating, place container registry in each region where images are run

#### Overview - Container Images

- Azure Container Registry (ACR) is a managed Docker registry service hosted in azure to build, store, and manage images for containers
- Container images can be pushed and pulled with Container Registry using Docker CLI or Azure CLI

#### High Level Process for Creating Container Image
  
- Create a directory for the new image - contains docker file and dependencies
- Create Docker File - contains the definition for the image
- Command line - run Docker Image
- Create container image - use docker build to create the image and add a tag
- list the newly created image

### *Publish an Image to Azure Container Registry (ACR)*

#### **CLI Commands** - Publish Image to ACR
  
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

### Overview - ACR
  
- Azure Container Registry Use Cases
  - Pull images from container registry to deployment targets (orchestration systems like K8s, Azure services like AKS)
  - Push to container registry as part of a container development workflow (CI)
  - Configure ACR Tasks to automatically rebuild application images. Automate building, testing, and patching images in parallel
  
#### **ACR Service Tiers**
  
- Basic - dev / learning. Same abilities as higher tiers but lower storage and image throughput
- Standard - Same capabilities but production level storage and image throughput
- Premium - Highest storage and concurrent operation. Adds geo-replication, image signing, and private endpoints

#### ACR Supported artifacts

- read-only snapshot of Docker compatible container (Windows / Linux)
- container rleated content (Helm charts and images to OCI Image format specification)

#### Storage Capabilities

- Encryption-at-rest
- Geo-Replication (Premium feature must be enabled)
  - replicate container registry in each region where images run
  - Single registry/image/tag names used accross multiple regions
  - Network-close registry access from regional deployments
  - No additional egress fees, images are pulled from local replicated registry
  - Siungle management of a registry across regions
- Zone redundancy - minimum of three zones (Premium service tier)
- Scalable storage - many repositories, images, layers, or tags up to the registry storage limit

#### ACR Authentication

- ACR doesn't support unauthenticated access and requires auth for all operations
- supports two typed of Identities
  - Azure Active Directory Identities (user and service principals)
  - Admin Account (included with each registry and disabled by default)

#### ACR Tasks

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

#### ACR Docker File

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

#### **CLI Commands** - Run Container Instance

- Deploy a container instance using Azure CLI

```bash
az group create --name az204-aci-rg --location <mylocation>
```

- Create container (name, docker image, and azure rg)
- Create DNS name to expose container to internet

```bash
DNS_NAME_LABEL=aci-example-$RANDOM
```

- start container instance (basic sample nodejs container)

```bash
az container create --resource-group az204-aci-rg \
--name mycontainer \
--image mcr.microsoft.com/azuredocs/aci-helloworld \
--ports 80 \
--dns-name-label $DNS_NAME_LABEL --location <mylocation> \
```

- Specify container restart policy

```bash
az container create \
--resource-group myResourceGroup \
--name mycontainer \
--image mycontainerimage \
--restart-policy OnFailure
```

- Provide environment variables

```bash
az container create \
--resource-group myResourcegroup \
--name mycontainer2 \
--image mcr.microsoft.com/azuredocs/aci-wordcount:latest \
--restart-policy OnFailure \
--environment-variables 'NumWords'='5' 'MinLength'='8' \
```

- create container from yaml

```bash
az container create --resource-group myResourceGroup \
--file secure-env.yaml \
```

- Deploy container and Mount Volume

```bash
az container create \
--resource-group $ACI_PERS_RESOURCE_GROUP \
--name hellofiles \
--image mcr.microsoft.com/azuredocs/aci-hellofiles \
--dns-name-label aci-demo \
--ports 80 \
--azure-file-volume-account-name $ACI_PERS_STORAGE_ACCOUNT_NAME \
--azure-file-volume-account-key $STORAGE_KEY \
--azure-file-volume-share-name $ACI_PERS_SHARE_NAME \
--azure-file-volume-mount-path /aci/logs/
```

- verify container

```bash
az container show --resource-group az204-aci-rg \
--name mycontainer \
--query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" \
--out table \
```

- Delete everything

```bash
az group delete --name az204-aci-rg --no-wait
```

#### **Things to remember** - Container Instances

- Due to YAML's more concise nature, a YAML file is recommended when a deployment includes only container instances (as opposed to ARM)
- YAML (reccomended) or ARM is requried when deploying a multi-container group. ```az container create``` will is suited only for single container
  
#### Containerized Tasks Restart Policies

- ACI stops containers when application or script exit. When policy is ```Never``` or ```OnFailure``` the container status is set to *Terminated*
- Policy Types
  - Always - Containers in container group always restarted (**default policy**)
  - Never - Containers are never restarted. Run *at most* once
  - OnFailure - Containers are restarted only when the process executed in the container fails (non-zero exit). Run *at least* once.

#### Container Instances Environmental variables

- Environmental variables in container intances allows for dynamic configuration of the application or script run by the container
- Secure values hold sensitive information (keys / pws)
  - Only accessible within the container
  - specify as ```secureValue``` instead of ```value```
  - Example in container YAML

  ```YAML
  apiVersion: 2018-10-01
  location: eastus
  name: securetest
  properties:
    containers:
    - name: mycontainer
      properties:
        environmentVariables:
          - name: 'NOTSECRET'
            value: 'my-exposed-value'
          - name: 'SECRET'
            secureValue: 'my-secret-value'
        image: nginx
        ports: []
        resources:
          requests:
            cpu: 1.0
            memoryInGB: 1.5
    osType: Linux
    restartPolicy: Always
  tags: null
  type: Microsoft.ContainerInstance/containerGroups
  ```

#### Mount Azure file share in Azure Container Instances (ACI)

- ACI are stateless by default. Persisted data must be written to a mount volume
- ACI can mount an Azure File Share created with Azure Files via SMB
- Limitations
  - Only mountable to **Linux** containers
  - Requires Linux container to run as root
  - Limited to CIFS support
- Example YAML template

```bash
apiVersion: '2019-12-01'
location: eastus
name: file-share-demo
properties:
containers:
- name: hellofiles
  properties:
    environmentVariables: []
    image: mcr.microsoft.com/azuredocs/aci-hellofiles
    ports:
    - port: 80
    resources:
      requests:
        cpu: 1.0
        memoryInGB: 1.5
    volumeMounts:
    - mountPath: /aci/logs/
      name: filesharevolume
  osType: Linux
  restartPolicy: Always
  ipAddress:
    type: Public
    ports:
      - port: 80
    dnsNameLabel: aci-demo
  volumes:
  - name: filesharevolume
    azureFile:
      sharename: acishare
      storageAccountName: <Storage account name>
      storageAccountKey: <Storage account key>
  tags: {}
  type: Microsoft.ContainerInstance/containerGroups
```

- You must use a YAML file (reccomended) or ARM template to mount multiple volumes (not CLI)

```yaml
"volumeMounts": [{
"name": "myvolume1",
"mountPath": "/mnt/share1/"
},
{
  "name": "myvolume2",
  "mountPath": "/mnt/share2/"
}]
```

- ARM Example

```json
"volumes": [{
"name": "myvolume1",
"azureFile": {
  "shareName": "share1",
  "storageAccountName": "myStorageAccount",
  "storageAccountKey": "<storage-account-key>"
}
},
{
  "name": "myvolume2",
  "azureFile": {
    "shareName": "share2",
    "storageAccountName": "myStorageAccount",
    "storageAccountKey": "<storage-account-key>"
  }
}]
```

## 1.2 Create Azure App Service Web Apps

### *Create an Azure App Service Web App*

#### **CLI Commands** - Create App Service Web App

- Retrieve list of linux runtimes

```bash
az webapp list-runtimes --os-type linux
```

- Find Outbound IPs

```bash
az webapp show \
  --resource-group <rg_name> \
  --name <app_name> \
  --query outboundIpAddress \
  --output tsv
```

- Get all possible outbound IP addresses for app

```bash
az webapp show \
  --resource-group <group_name> \
  --name <app_name> \
  --query possibleOutboundIpAddresses \
  --output tsv
```

- Deploy simple html web app (same command to redeploy)

```bash
az webapp up --resource-group <rg_name> --name <app_name> --html
```

#### **Important Notes** - App Service Web App

- The Consumption App Service Plan **only** supports function apps
- Know the Inbound / Outbound control features

#### Overview - Create App Service Web App

- Azure App Service is a PaaS to assis with developing applications w/out worrying about infrastructure
- Based on HTTP
- App Service Plan manages the group of VMs that run the application
- You ~~cannot~~ can (as of Jan 21, 2021) mix Windows and Linux apps in the same resource group in the same region
- Setup Info
  - Basic - Region, Number of Instances, Size of Instances, OS platform, Pricing Tier
  - Auth - Azure, Microsoft, Google, Facebook, etc.
- Integration with on-premise infrastructure
  - VNet Integration - allows web app to access resource in your vnet (or on prem via site to site vpn)
  - Hybrid connections - Azure Service Bus Relay creates a network connection between App Service and Application Endpoint (specific IP / Port combo)
- Benefits
  - Built-in auto scale support
  - CI/CD support and integration (AzDo, GitHub, Bitbucket, FTP, or local Git repo)
  - Deployment slots (dev vs prod)

#### App Service Plans

- Shared Compute - Free and Shared share the resource pools of your apps with other customers. No scale out
- **Dedicated compute** - Basic, Standard, Premium, PremiumV2, and PremiumV3 run apps on dedicated Azure VMs. Scale out is available
- **Isolated** - runs dedicated Azure VMs on dedicated Azure Virtual Networks. Network Isoluation and maximum scale-out capabilities.
- **Consumption** - only available to *function apps* it scales the functions dynamically to workload

#### Running and Scaling App Service

- App Service plan is the scale unit of the App Service apps
- Diagnostic logs, backups, and WebJobs also use CPU cycles and memory
- Apps of the same service plan share compute resources
- Isolate app if it is resource-intensive, you want to scale independently, or needs a different geo region

#### App Service Web App Deployment

- Deployment Types
  - Automated deployment (CI) - Azure DevOps, GitHub, Bitbucket
  - Manual Deployment - Git (url as remote repo), CLI (```az webapp up```), Zip deploy, FTP/S
- Deployment slots
  - Use deployment slots when deploying prod build
  - deploy app to staging environment then swap staging and production slots
  - warms up worker instances and eliminates downtime

#### App Service Web App Authentication

- When authentication and authorization are enabled with a provider, every incoming http request passes through it before being handled by application code
- Provides - Authentication, Validation / refresh of tokens, session management, injects identity into headers
- Auth Flow
  - All: Sign User In -> Post-Authentication -> Establish Authed Session -> Serve Authed content
  - Without Provider SDK: application delegates federated sign-in to App Service. Like a browser app, presents the providers login page. The **server code** manages the sign-in Process. aka **server-directed flow** or **server flow**
  - With Provider SDK: application signs users in to the provider manually then submits auth token to App Service for validation. Browserless apps which can't provide sign-in page to user. The **application code** manages the sign-in process. aka **client-directed flow** or **client flow**. applies to REST APIs, Azure Functions, JavaScript browser clients, and native mobile apps
- AuthZ behavior options
  - Allow unauthenticated requets - more flexibility, allows for presenting multiple sign-in providers
  - Require Authentication - reject any unauthenticated traffic

#### App Service Networking Features

- By default, apps hosted in App Service are accessible directly via the internet
- Two Deployment Types
  - Multitenant public service - Free, Shared, Basic, Standard, Premium, PremiumV2, and PremiumV3
  - Single-Tenant App Service Environment (ASE) - Host isolated SKU App Service plans directly in Azure Virtual Network
- Multi-Tenant App Service Networking Features
  - *front ends* - handle incoming HTTP or HTTPS requests
  - *workers* - handle customer workloads
  - You can't connect multi-tenant App Service network directly to your own network. Instead use features to handle comms
  - Inbound Features
    - App-Assigned Address
    - Access Restrictions
    - Service Endpoints
    - Private Endpoints
  - Outbound Features
    - Hybrid Connections
    - Gateway-required virtual network integration
    - Virtual network integration
  - Scaling Considerations
    - worker VMs are broken down by App Service plans
    - if you scale service plans (e.g. PremiumV2 to PremiumV3) your outbound addresses will change
    - To see all addresses an app may use in a scale set unit check the ```possibleOutboundAddresses``` property

#### Resources - Create Azure App Service

- [Create an ASP.NET Core web app in Azure](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-dotnet)
- [Explore Azure App Service](https://docs.microsoft.com/en-us/learn/modules/introduction-to-azure-app-service/)

### *Enable Diagnostics Logging*

#### **CLI Commands**

- Enable app logging to the file system

```bash
az webapp log config --application-logging true --level verbose --name <app-name> --resource-group <rg-name>
```

- Reset File System Logging to error-level only

```bash
az webapp log config --application-logging false --name <app-name> --resource-group <rg-name>
```

- View current logging status for an app

```bash
az webapp log show --name <app-name> --resource-group <rg-name>
```

- Create App Service Plan and webapp

```bash
az appservice plan create --name $appPlan --resource-group $resourceGroup --location $appLocation --sku FREE
az webapp create --name $appName --resource-group $resourceGroup --plan $appPlan --deployment-source-url $gitRepo
```

- Create Storage Account

```bash
az storage account create -n $storageAccount -g $resourcegroup -l $appLocation --sku Standard_LRS
```

- Open Log Stream for Web App

```bash
az webapp log tail --name <app name> --resource-group <rg_name>
```

- reset user-level credentials (Username must be globally unique)

```bash
az webapp deployment user set --user-name <name-of-user-to-create> --password <new-password>
```

- Open Log Stream with curl

```bash
curl -u {username} https://{sitename}.scm.azurewebsites.net/api/logstream
```

- Download file system logs (copy to cloud shell storage then run the following)

```bash
az webapp log download --log-file \<_filename_\>.zip --resource-group <rgname> --name <app-name>
```

#### Overview - Web App Diagnostics
  
- App logs for Azure Apps are teh output of runtime trace statements in app code
- App logging is primarily for apps in pre-production and for troublesome issues because excessive logs carry performance / storage hit
- logging to file system is auto-disabled after 12 hours

#### Available Logging by Framework

- ASP.Net
  - Windows Only
  - ```System.Diagnostics.Trace```
  - Levels - ```error```, ```warning```, ```information```, and ```verbose```
  - ```Trace.TraceError("Message"); // Writes an error message```
  - ```Trace.TraceWarning("Message"); // Writes a warning message```
  - ```Trace.TraceInformation("Message"); // Writes an information message```
  - ```Trace.WriteLine("Message"); // Writes a verbose message```
- ASP.NET Core Apps
  - Windows and Linux
  - **logger factory class**
  - ```logger.LogCritical("Message"); // Writes a critical message at log level 5```
  - ```logger.LogError("Message"); // Writes an error message at log level 4```
  - ```logger.LogWarning("Message"); // Writes a warning message at log level 3```
  - ```logger.LogInformation("Message"); // Writes an information message at log level 2```
  - ```logger.LogDebug("Message"); // Writes a debug message at log level 1```
  - ```logger.LogTrace("Message"); // Writes a detailed trace message at log level 0```
  - Verbose (0-1), Information (2), Warning (3), Error (4-5)
- Node.js Apps
  - Enabled using **console()**
  - ```console.error("Message")``` - writes to STDERR
  - ```console.log("Message")``` - writes to STDOUT
  - both STDERR and STDOUT are written to app service error-level logs
- Logging Windows vs Linux Hosts
  - Windows-based web apps is integrated with the underlying IIS service (saves to File System, Blob Storage)
  - Linux-based apps relies on the Docker image used and redirects to STDERR or STDOUT use the Docker Logs (saves to File System Only)
  - Types of logging for Windows vs Linux
    - Application Logging - Windows & Linux
    - Deployment Logging - Windows & Linux
    - Web Server Logging - Windows ONLY
    - Detailed error logging - Windows ONLY
    - Failed request tracing - Windows ONLY
- Log File Locations
  - Windows
    - D:\Home\LogFiles
      - Application - application generated messages if **File System logging** has been enabled
      - DetailedErrors - Contains detailed Web Server error logs, if **Detailed** error messages have been enabled
      - http - Contains IIS-level logs, if **Web Server Logging** has been enabled
      - W3SVC\<Number\> - Details of all failed https requests, if **Failed request tracing** has been enabled
    - Stored in year, month, date, and hour folders - one or more CSV files containing messages saved within 60 minute period
  - Linux
    - Redirections to STDERR and STDOUT are managed through the Docker container
    - Stored in Docker log files
    - Need to open an SSH connection to the docker container
  - Retrieval
    - Azure CLI
    - Kudu (central service site)
    - Azure storage explorer

#### Alternatives

- Azure Application Insights (with SDK and Instrumentation Key)
- Azure Monitor (for CPU, memory, network, and file system useage only)

#### Live Log Streaming

- Easy way to view live logs via command line
- Shows a redirect from the file system logs
- Useful for initial debugging, only connects to a single app instance
- Enable via Azure CLI, Curl, or Azure Portal UI
  
#### Enable Logging (Portal)

- Set **Application Logging (Filesystem)** on and set the Level
- Set **Application Logging (Blob)** on and set Level
  - Not avaialable in Linux app logs
  - Must set a Retention Period

#### Resources

- [Enable diagnostics logging for apps in Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)
- [Capture Web Application Logs with App Service Diagnostics Logging (Module)](https://docs.microsoft.com/en-us/learn/modules/capture-application-logs-app-service)
  
### *Deploy Code to a Web App*

#### **CLI Commands** - Deploy Web App

- Create Rg, App Service Plan, and Web App from service plan

```bash
# Create a resource group
az group create --location eastus2 --name myapp-rg

# Create an app service plan of type Windows
az appservice plan create -g myapp-rg -n myapp-service-plan

# Create an App Service from the plan 
az webapp create -g myapppipeline-rg -p myapp-service-plan -n my-app-dotnet-win --runtime "DOTNETCORE|3.1"
```

- Create .NET webapp

```.NET CLI
dotnet new webapp -f net6.0
```

- Run the application locally

```.NET CLI
dotnet run
```

- Deploy a ZIP Package

```bash
# Push Deploy
az webapp deploy --resource-group <rg-name> --name <app-name> --src-path <zip-package-path>

# Pull Deploy (if AppService is locked down)
az webapp deploy --resource-group <rg-name> --name <app-name> --src-url "<url-to-zip>"
```

- By default the ZIP is assumed ready to run as is, to enable build for the zip

```bash
az webapp config appsettings set --resource-group <rg-name> --name <app-name> --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

#### Tips to Remember - Deploy Code to a Web App

- To specify a virtual application to deploy to in YAMLl use ```VirtualApplication``` property of ```AzureRmWebAppDeployment``` task
- Azure DevOps task is the ```AzureWebApp``` task

#### Overview - Deploy Code to a Web App

- Multiple Deployment Methods Including
  - Azure Pipelines
  - Azure CLI
  - ZIP / WAR File

#### Azure DevOps Pipelines

- Process  
  - Create the Resource Group, App Service Plan, and Webapp
  - Create the .Net project
  - Upload the doe to GitHub or Azure DevOps Repository
  - Establish Service Connection for credentials
  - Create an Azure Devops Pipeline with a **Azure Web App** task (example task YAML)

  ```YAML
  - task: AzureWebApp@1
  inputs:
    azureSubscription: '<Azure service connection>'
    appName: '<Name of web app>'
    package: $(System.DefaultWorkingDirectory)/**/*.zip 
  ```

- Example of full pipeline for .NET app

```YAML
variables:
buildConfiguration: 'Release'

steps:
- script: dotnet build --configuration $(buildConfiguration)
  displayName: 'dotnet build $(buildConfiguration)'
- task: DotNetCoreCLI@2
  inputs:
    command: 'publish'
    publishWebProjects: true
- task: AzureWebApp@1
  inputs:
    azureSubscription: '<Azure service connection>'
    appType: 'webAppLinux'
    appName: '<Name of web app>'
    package: '$(System.DefaultWorkingDirectory)/**/*.zip'
```

#### Using Deployment Slots

- Deployment slots are separate slots than the default production slot
- Benefits
  - You can validate app changes in staging before swapping to production
  - Deploying to a slot first then swapping it to production makes sure the instace is warmed up (elminates downtime)
  - You can configure auto swap when pre-swap validation isn't needed
  - After a swap the previous production app is now staged and can be swapped back to get "last known good"
- Available in **Standard**, **Premium**, or **Isolated** App Service plan tiers
- High Availability features of swap (performed by Azure)
  - apply settings from target slot to all instances of source slot (connection strings, CD settings, auth settings)
  - Wait for every instance in source slot to complete restart
  - Trigger local cache initialization
  - Trigger application initiation if ```applicationInitiallization``` is specified (e.g. makes an HTTP request to the application)
  - Once warm, swap the two slots by switching the routing rules for the two slots
- Swap Types
  - Manual swap - go to app deployment slots and swap
  - Swap with Preview (multi-phase swap) - Before you swap, validate the app runs with swapped settings
  - Configure Auto-Swap - Everytime you push code changes to specified slot, App Service automatically swaps the app into production after warm up (*Not available in Linux web apps*)
- Custom Warm-up
  - Use the ```applicationInitialization``` element in the web.config to specify initialization pages
  - ```WEBSITE_SWAP_WARMUP_PING_PATH``` - Path to ping to warm up site (e.g. /statuscheck)
  - ```WEBSITE_SWAP_WARMUP_PING_STATUSES``` - Valid HTTP response codes for warm-up operation, if valid status isn't returned the warmup and swap operations are stopped
- Appears in log query as ```Swap Web App Slots```
- Production traffic can be routed to multiple slots
  - Look at header ```x-ms-routing-name``` cookie value to determine slot user is routed to
  - Route automatically by Traffic % then pinned for the life of that session
  - Route traffic manually (e.g. to let users opt in / out of a beta)

#### Resources - Deploy Code to a Web App

- [Explore Azure App Service Deployment Slots(Module)](https://docs.microsoft.com/en-us/learn/modules/understand-app-service-deployment-slots/)
- [Deploy an Azure Web App](https://docs.microsoft.com/en-us/azure/devops/pipelines/targets/webapp)
- [Deploy your app to Azure App Service with a ZIP or WAR file](https://docs.microsoft.com/en-us/azure/app-service/deploy-zip)
- [Provision and deploy microservices predictably in Azure](https://docs.microsoft.com/en-us/azure/app-service/deploy-complex-application-predictably)

### *Configure Web App Settings Including SSL, API Settings, and Connection Strings*

#### *CLI Commands* - Configure Web App Settings

- For a definitive list of the connection string types, run the following command in Azure PowerShell

```PowerShell
[Enum]::GetNames("Microsoft.WindowsAzure.Commands.Utilities.Websites.Services.WebEntities.DatabaseType")
```

- Merge intermediate certs in cert chain prior to upload

```bash
openssl pkcs12 -export -out myserver.pfx -inkey <private-key-file> -in <merged-certificate-file>
```

#### Web App Settings Overview

- App Service settings are passed as environmental variables to application code
  - In Linux / Custom containers passed using the ```--env``` flag
  - In ASP .NET and .NET Core settings are in ```<appSettings>``` in *Web.config* or *appsettings.json*
  - Access settings from app management page **Configuration** -> **Application Settings**
- Add single new setting from configuration page
- Add bulk settings using json file
- App Service settings **override** *Web.config* settings
- To apply only to development slot enable as *slotSetting*

#### General Web App Settings

- **Stack Settings** - software stack to run the app, including laguage and SDK version. Specify optional start-up cmd or file
- **Platform Settings** - Configure settings for hosting platform, including
  - **Bitness** - 32 bit vs 64 bit
  - **WebSocket Protocol** - e.g. for ASP .NET SignallR or socket.io
  - **Always On** - Keep the app loaded even when there's no traffic. By default app is unloaded after 20 minutes of no requests. Required for WebJobs.
  - **Managed pipeline version** - IIS pipeline mode. set to **Classic** if you have a legacy app requiring an older version of IIS.
  - **HTTP version** - 1.0 or 2.0
  - **ARR affinity** - In a multi-instance deployment, ensure that the client is routed to the same instance for the life of the session. Set to Off for *stateless applications*
- **Debugging** - Enablle remote debugging for ASP.NET, ASP.NET Core, or Node.js apps. Automatically turns off after **48 hours**
- **Incoming client certificates** - require client certificates in mutual authentication. TLS mutual authentication is used to restrict access to your app by enabling different types of authentication for it.

#### Web App Path Mappings

Path mappings configure handler mappings, and virtual application and directory mappings. Differnt options based on OS type

- Windows apps (uncontainerized)
  - **Extension** - file extension to handle such as *.php or handler.fcgi
  - **Script Processor** - The absolute path of the script processor. Requests to files that match the extension are processed by the script processor
  - **Arguments** - Optional command-line arguments for the script processor
- Linux and containerized apps
  - **Name** - display name
  - **Configuration options** - Basic or Advanced
  - **Storage accounts** - storage account with the container you want
  - **Storage type** - Azure Blobs or Azure Files (Windows container apps onlly support Azure Files)
  - **Storage container** - The container you want (basic config)
  - **Share name** - File Share name (Adv config)
  - **Access key** - Access Key (Adv config)
  - **Mount path** - Absollute path in your container to mount the custom storage

#### Configure Web App Security Certificates

Azure App service has tools to create, upload, or import a private cert or public cert into App Service

- A cert uploaded into an app is stored in a deployment unit bound to the app service plan resource group and region combo (i.e. *webspace*). This makes the cert accessible to other apps in the same *webspace*
- Options for adding certs in App Service
  - Create a free App Service managed cert
  - Purchase an App Service certificate
  - Import a certificate from Key Vault
  - Upload a private certificate
  - upload a public certificate
- Private Cert Requirements
  - Exported as password-protected PFX file encrypted with triple DES
  - private key at least 2048 bits long
  - Contains all intermediate certs in the chain
  - Contains Extended Key Useage for Server Auth (custom domain TLS binding)
  - Signed by trusted cert authority (custom domain TLS binding)
- HTTP is allowed by default, setting available to enforce https only

#### Configure App Features (Feature Flags)

Feature flags decouples feature release from code deployment allowing quick changes (e.g. feature toggles, floags, switches, etc.)

- Feature Flag = Name and One or More Filters
- App Service Feature manager
  - supports *appsettings.json* as a configuration source for feature flags
  - Azure App Configuration overrides appsettings.json / web.config and is designed to be a central repository for feature flags
- Use the App Configuration libraries to access the feature flags from the application

#### Resources - Configure Web App Settings

- [Configure Web App Settings (Module)](https://docs.microsoft.com/en-us/learn/modules/configure-web-app-settings/)
- Custom configuration and application settings in Azure Web Sites
- [Configure an App Service app in the Azure portal](https://azure.microsoft.com/en-us/resources/videos/configuration-and-app-settings-of-azure-web-sites)
- [Buy a custom domain name for Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/configure-common)
- [Add a TLS/SSL certificate in Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/configure-ssl-certificate)

### *Implement Autoscaling Rules Including Scheduled Autoscaling and Autoscaling by Operational or System Metrics*

#### **CLI Commands** Autoscaling

- Increase number of VM instances in scale set when average CPU load is greater than 70% over a 5-minute period

```bash
az monitor autoscale rule create \
  --resource-group myResourceGroup \
  --autoscale-name autoscale \
  --condition "Percentage CPU > 70 avg 5m" \
  --scale out 3
```

- Decrease number of VM instances in a scale set when the average CPU load drops below 30% over a 5-minute period

```bash
az monitor autoscale rule create \
  --resource-group myResourceGroup \
  --autoscale-name autoscale \
  --condition "Percentage CPU < 30 avg 5m" \
  --scale in 1
```

- manually scale app service to 2 workers

```bash
az appservice plan update --number-of-workers 2 --name $appServicePlan --resource-group $resourceGroup
```

#### Autoscaling Tips to Remember

- Autoscaling is a scale out / in solution
- Changes in application load that are predictable (i.e. more users on Friday) are good candidates for autoscaling
- "Grind system to halt" e.g. Denial of Service attack will **not** be handled by autoscaling
- Scale out operations trigger if **any** rule conditions are met
- Scale in Operations only trigger if **all** rule conditions are met

#### Overview - Implement Autoscaling

- Def: Autoscaling is the process of dynamicallly alllocating resources to match performance requirements.
  - Vertical Scaling - scale up / down (bigger / smaller vm)
  - Horzontal scaling - scale out / in (more / less vms)

#### Conditions, Metrics, and Actions for autoscale rules

- Conditions
  - Scale based on metric
  - Scale based on schedule
- Metrics
  - **CPU Percentage**
  - **Memory Percentage**
  - **Disk Queue Length**
  - **Http Queue Length**
  - **Data in**
  - **Data out**
- How autoscale analyzes metrics
  - aggregates the values for a metric for all instances over a *time grain*
  - available aggregates: Average, Minimum, Maximum, Total, Last, and Count 
  - calculates over a user-specified time value *Duration*
  - *Time Grain* is the period of calculation for a metric 
  - *Duration* is the aggregate 
  - The aggregation calculation for *Duration* can be differant from *time grain*
  
  > if the *time aggregation* is *Average* and the statistic gathered is CPU percentage across a one-minute *time grain*, each minute the average CPU percentage util across all instances for that minute will be calculated. If the *time grain statistic* is set to *Maximum* and the *Duration* of the rule is set to 10 minutes, the maximum of the 10 average values for CPU percentage utilization will be used to determin if the threshold has been crossed.

- Autoscale actions
  - scale out or scale in by a specified increment
  - cannot exceed the max instances for the App Service plan
  - autoscale action has a cool down period - minimum 5 minutes
  - if combining rules, scale out occurs if any threshold is passed
  - if combining rules, scale in occurs only if under all thresholds

#### Enable App Service Autoscaling

- Enable autoscale
  - select *Custom autoscale*
  - add scale conditions
  - create scale rules
  - Monitor autoscale activity
- autoscale scales horizontally
- autoscale always reads the associated metric
- all thresholds are calculated at instance level
- autoscale sucess / failure are logged in activity log

### Autoscale best practices

- Ensure the Max and Min values are different and have adequatre margin between them
- Choose appropriate metrics
- Chose the thresholdls carefully (big enough margin to void flapping)
- Consider how scaling performs when multiple rules are configured in a profile
- Always select a safe default instance count (service default when metrics are unavailable)
- Configure autoscale notifications

#### Resources - Azure Autoscaling

- [Scale apps in Azure App Service (Module)](https://docs.microsoft.com/en-us/learn/modules/scale-apps-app-service/)
- [Azure Autoscaling Best Practices](https://docs.microsoft.com/en-us/learn/modules/scale-apps-app-service/)
- [Scale up an App in Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/manage-scale-up)
- [Get started with Autoscale in Azure](https://docs.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-get-started)
- [App Service Environment AutoScale](https://docs.microsoft.com/en-us/azure/app-service/environment/app-service-environment-auto-scale)

## 1.3 Implement Azure Functions

### *Create and Deploy Azure Function Apps*

#### Overview - Azure Functions

Azure Functions are serverless compute service that enable processing data, integrating system, working with IoT, and building simple APIs.

- Azure Functions vs Logic Apps
  - Azure Functions require writing code, Logic Apps uses a GUI (primarilly)
  - Logic Apps uses a designer-first (declarative) development model
- Azure Functions Vs WebJobs
  - Azure Functions is built on the WebJobs SDK but allows for serverless app model and automatic scaling

#### Azure Functions Plans
  
- Plan Options
  - **Consumption Plan**
    - Default Plan
    - Scales automatically 
    - Only pay for compute resources when functions are running
  - **Premium Plan**
    - Automatically scales based on demand using pre-warmed workers which run with no delay after being idle
    - More powerful instances
    - Connects to VNets
  - **Dedicated Plan**
    - Run functions within App Service plan
    - Best for long-running scenarios not suitable for Durable Functions
    - enable **Always on** so function app runs correctly
- Hosting Options
  - **App Service Environment (ASE)**
    - fully isolated and dedicated environment
    - running App Service apps at high scale
    - Supports setting autoscaling rules based on predictive usage
  - **Kubernetes**
    - fully isolated and dedicated environment
- *All plans require a general Azure Storage account*

#### Azure Functions Development

- Function contains two important pieces
  - *Code* - written in varity of languages
  - *Config* - the function.json file (generated automatically for compiled languages)

  ```json
  {
      "disabled":false,
      "bindings":[
          // ... bindings here
          {
              "type": "bindingType",
              "direction": "in",
              "name": "myParamName",
              // ... more depending on binding
          }
      ]
  }
  ```

- Function app provides execution context
  - One or more individual functions
  - managed, deployed, and scaled together
  - same pricing plan, deeployment method, and runtime version
  - *In Functions 2.x* - all lfunctions must be authored in the same language
- Folder structure
  - code for all the functions in a function app is located in a root project folder
  - *host.json* contains runtime-specific configs and is the root folder
  - *bin* folder contains packages and other library files required by the function app

#### Scale Azure Functions

- In *Consumption* and *Premium* plans, Azure Functions scales by adding additional instances of the Functions host
- Runtime Scaling - Azure functions uses the *scale controller* to monitor function rate and determine if scale out is needed
- Cold Start - If function app is idle for a number of minutes, the platform may scale instances down to 0
- Scaling behaviors
  - **Maximum instances**
    - Consumption Plan - Single function app scales to a max of 200 instances
    - Premium Plan - Single function scales to a max of 100 instances (more powerful intance)
    - Specify lower limit by setting ```functionAppScaleLimit```
  - **New instance rate**
    - HTTP triggers - new instances allocated at most *once per second*
    - Non-HTTP triggers - new instances allocated at most *once per 30 seconds*

#### Resources - Deploy Azure Function Apps

- [Explore Azure Functions (Module)](https://docs.microsoft.com/en-us/learn/modules/explore-azure-functions/)
- [Getting Started with Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-get-started?pivots=programming-language-csharp)
- [Folder Layout for Compiled C# Functions Apps](https://docs.microsoft.com/en-us/azure/azure-functions/functions-dotnet-class-library?tabs=v2%2Ccmd#functions-class-library-project)
- [Develop and Test Azure Functions Locally](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-local)
- [dotnet Isolated Process Guide](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide)
  
### *Implement Input and Output Bindings for a Function*

#### Overview Input and Output Bindings

- *Triggers* are what cause a function to run, a function must have exactly one trigger
- *Bindings* to a function is a way of declaratively connecting another resource to the function
  - can be *input binding*, *output binding*, or *both*
  - Data from bindings is provided to the function as parameters
- The ```bindings``` property of the function.json file is where you configure triggers and bindings
  - ```type``` - string - Name of binding ex ```queueTrigger```
  - ```direction``` - string - indicate direction of data ```in``` or ```out```
  - ```name``` - string - the name that is used for the bound data in the function ex ```myQueue```
  
#### Create Triggers and Bindings

- Trigger and binding code definitions
  - C# class library - decorating methods and parameters with C# attributes
  - Java - decorating methods and parameters with java annotations
  - JavaScript/PowerShell/Python/TypeScript - updating *function.json* schema
    - example

    ```json
    {
      "dataType": "binary",
      "type": "httpTrigger",
      "name": "req",
      "direction": "in"
    }
    ```

- Trigger and Binding example
  - Write a new row to Azure Table storage whenever a new message appears in Azure Queue storage
  - function.json

  ```json
  {
    "bindings": [
      {
        "type": "queueTrigger",
        "direction": "in",
        "name": "order",
        "queueName": "myqueue-items",
        "connection": "MY_STORAGE_ACCT_APP_SETTING"
      },
      {
        "type": "table",
        "direction": "out",
        "name": "$return",
        "tableName": "outTable",
        "connection": "MY_TABLE_STORAGE_ACCT_APP_SETTING"
      }
    ]
  }
  ```

- Trigger and Binding Example (C# Script)
  - used in conjunction with above function.json file

    ```C#
    #r "Newtonsoft.Json"

    using Microsoft.Extensions.Logging;
    using Newtonsoft.Json.Linq;

    // From an incoming queue message that is a JSON object, add fields and write to Table storage
    // The method return value creates a new row in Table Storage
    public static Person Run(JObject order, ILogger log)
    {
        return new Person() { 
                PartitionKey = "Orders", 
                RowKey = Guid.NewGuid().ToString(),  
                Name = order["Name"].ToString(),
                MobileNumber = order["MobileNumber"].ToString() };  
    }

    public class Person
    {
        public string PartitionKey { get; set; }
        public string RowKey { get; set; }
        public string Name { get; set; }
        public string MobileNumber { get; set; }
    }
    ```

- Trigger and Binding Example (C# compiled class libarary)
  - trigger and binding information proveded by attributes **not** function.json file
  - example
  
  ```C#
  public static class QueueTriggerTableOutput
  {
      [FunctionName("QueueTriggerTableOutput")]
      [return: Table("outTable", Connection = "MY_TABLE_STORAGE_ACCT_APP_SETTING")]
      public static Person Run(
          [QueueTrigger("myqueue-items", Connection = "MY_STORAGE_ACCT_APP_SETTING")]JObject order,
          ILogger log)
      {
          return new Person() {
                  PartitionKey = "Orders",
                  RowKey = Guid.NewGuid().ToString(),
                  Name = order["Name"].ToString(),
                  MobileNumber = order["MobileNumber"].ToString() };
      }
  }

  public class Person
  {
      public string PartitionKey { get; set; }
      public string RowKey { get; set; }
      public string Name { get; set; }
      public string MobileNumber { get; set; }
  }
  ```

#### Connection Azure Functions to Azure Services

- Multi-Environment safety
  - Function project references connection information by name from configuration provider
  - Don't set directly in function.json, instead you would set *connection* property to the name of an environmental variable
  - connection string typicallly also includes a secret
- Configure Identity-Based Connections
  - *Not supported with Durable Functions*
  - When hosted in Azure Functions service, identity-based connections use a *managed identity*
  - System identity is used by defaullt, but a user-assigned identity can be specified ```credential``` and ```clientID```

#### Resources - IO Bindings for a Function

- [Develop Azure Functions (Module)](https://docs.microsoft.com/en-us/learn/modules/develop-azure-functions/)
  
### *Implement Function Triggers by Using Data Operations, Timers, and Webhooks*

#### Overview - Azure Function Triggers

Triggers are what invokes an Azure Function. Every function must have exactly one trigger associated with it. If you want to execute an identical piece of logic with a different trigger, you need to create multiple identical functions with different triggers. The following are the most commonly Used

- Common Triggers
  - **Generic Webhook** - Fired in the case of HTTP requests that come from a service that supports webhooks
  - **GitHub Webhook** - Fired in the case of any events like Branch creation, delete, comment, commit, etc.
  - **Timer** - Execute function at set interval
  - **HTTP** - Execute when an HTTP request is received
  - **Blob** - Execute when a file is uploaded or updated in Blob Storage
  - **Queue** - Execute a function when a message is added to an Azure Storage queue
  - **Azure Cosmos DB** - Execute when a document changes in a colllection
  - **Event Hub** - Execute a function when an event hub reeceives a new event

#### Trigger Azure Function on Timer

A timer trigger is a trigger that executes a function at a consistent interval

- Timer trigger requirements
  - *Timestamp parameter name* - identifier to access the trigger in code
  - *Schedule* - CRON expression that sets interval for the timer
- **Azure CRON expression**
  - six fields
  - ```{second} {minute} {hour} {day} {month} {day of the week}```
  - ex every five minutes ```0 */5 * * * *```
  - character meanings
    - ```*``` wild card 
    - ```,``` list separator
    - ```-``` range specifier
    - ```/``` specifies an increment 
- Creating the timer-triggered function in Azure with the name and schedule will invoke the function to fire

#### Trigger Azure Functions with HTTP Request

An HTTP request is a common operation to invoke Azure functions.

- HTTP trigger requirements
  - Programming Language
  - Trigger Name
  - Authorization Level
- Common HTTP Triggers customizations
  - Provide authorized access by supplying **keys**
  - Restrict supported HTTP verbs
  - Return data back to caller
  - Receive data through query string parameters or request body
  - Support URL route templates to modify the function URL
- HTTP Trigger Authorization level
  - flag to indicate if an incoming HTTP request needs an API key for auth
  - Three Levels
    - Function - key based. Use *function* key (specific function) or *host* key (apply to all function in app)
    - Anonymous - no auth
    - Admin -key based. Must provide *host* key
- *Request Parameter Name* - setting in trigger creation that represents the name of the parametyer that contins the information about an incoming HTTP request. Default is *req*
- Example *function.json* file for http trigger binding

```json
{
    "bindings": [
        {
            "authLevel": "function",
            "type": "httpTrigger",
            "direction": "in",
            "name": "req",
            "methods": [
                "get",
                "post"
            ]
        },
        {
            "type": "http",
            "direction": "out",
            "name": "res"
        }
    ]
}
```

#### Trigger Azure Function with Data Operation

Trigger a function when a file is uploaded or updated in storage

- Creating Blob trigger
  - **Path** - tells the blob trigger where to monitor. 
    - Default value is ```samples-workitems/{name}```
    - ```samples-workitems``` is the blob container
    - ```{name}``` every type of file will cause the trigger to invoke the function
    - ```{name}.png``` - would filter to onlly .png files
    - ```name``` is the parameter that the Azure function receives the file name string as

#### Trigger Azure Function with Webhook

Webhooks are a lightweight mechanism for apps to be notified (via HTTP) by another service when something of interest happens. Aka *user-defined HTTP callbacks*

- When the webook runs, it sends a payload request to the URL of the Azure Function
- Setup webhook for Github Repository
  - Setup webhook on github repository (per Github docs)
  - Provide payload url of the Azure function server
  - Trigger and parse payload with Azure function then send response
  - Validate response in Github
- Copy Azure function URL by selecting **Get Function URL** from command bar
- Secure Webhook payloads with a secret
  - Webhook secrets used to sign payloads and are received in ```x-hub-signature``` of the POST request
  - Hashed webhook payload validation needs to be handled by the Azure Function code (manually)
  - Example validation in JavaScript

  ```JavaScript
  const Crypto = require('crypto');

  module.exports = async function (context, req) {
      context.log('JavaScript HTTP trigger function processed a request.');

      const hmac = Crypto.createHmac("sha1", "<default key>");
      const signature = hmac.update(JSON.stringify(req.body)).digest('hex');
      const shaSignature =  `sha1=${signature}`;
      const gitHubSignature = req.headers['x-hub-signature'];

      if (!shaSignature.localeCompare(gitHubSignature)) {
          if (req.body.pages[0].title) {
              context.res = {
                  body: "Page is " + req.body.pages[0].title + ", Action is " + req.body.pages[0].action + ", Event Type is " + req.headers['x-github-event']
              };
          }
          else {
              context.res = {
                  status: 400,
                  body: ("Invalid payload for Wiki event")
              }
          }
      }
      else {
          context.res = {
              status: 401,
              body: "Signatures don't match"
          };
      }
  };
  ```

#### Resources - Azure Function Triggers

- [Monitor GitHub events by using a webhook with Azure Functions (Module)](https://docs.microsoft.com/en-us/learn/modules/monitor-github-events-with-a-function-triggered-by-a-webhook/)
- [Execute an Azure Function with Triggers(Module)](https://docs.microsoft.com/en-us/learn/modules/monitor-github-events-with-a-function-triggered-by-a-webhook/)
- [Azure Functions triggers and bindings concepts](https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings)
- [Azure Functions trigger and binding example](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-example)
- [Azure Functions HTTP triggers and bindings overview](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook)

### *Implement Azure Durable Functions*

#### Overview - Durable Functions

*durable functions* define stateful workflows by writing *orchestrator functions*  and stateful entities by wirting *entity functions*. The exention manages state, checkpoints, and restarts, allowing the developer to focus on the business logic

- Primary Use case is simplifying complex, stateful, coordination in serverless applications
- Supported Languages
  - C#
  - JavaScript (Azure Function runtime 2.x)
  - Python
  - F#
  - PowerShell (Azure Function 3.X)

#### Durable Function Application Patterns

- **Function Chaining**
  - sequence of functions executes in specific order
  
  ![Function Chaining](../../Images/function-chaining.png)

  - Code example

  ```c#
  [FunctionName("Chaining")]
  public static async Task<object> Run(
      [OrchestrationTrigger] IDurableOrchestrationContext context)
  {
      try
      {
          var x = await context.CallActivityAsync<object>("F1", null);
          var y = await context.CallActivityAsync<object>("F2", x);
          var z = await context.CallActivityAsync<object>("F3", y);
          return  await context.CallActivityAsync<object>("F4", z);
      }
      catch (Exception)
      {
          // Error handling or compensation goes here.
      }
  }
  ```

- **Fan out/fan in**
  - execute multiple functions in parallel and then wait for all functions to finish
  - aggregation work is done and results returned from the functions
  - *Fan Out* - have the function send multiple messages to a queue
  - *Fan In* - Write code to track when the queue-triggered functions end then store outputs

  ![Fan Out / In](../../Images/fan-out-fan-in.png)

  - Code Example

  ```c#
  [FunctionName("FanOutFanIn")]
  public static async Task Run(
      [OrchestrationTrigger] IDurableOrchestrationContext context)
  {
      var parallelTasks = new List<Task<int>>();

      // Get a list of N work items to process in parallel.
      object[] workBatch = await context.CallActivityAsync<object[]>("F1", null);
      for (int i = 0; i < workBatch.Length; i++)
      {
          Task<int> task = context.CallActivityAsync<int>("F2", workBatch[i]);
          parallelTasks.Add(task);
      }

      await Task.WhenAll(parallelTasks);

      // Aggregate all N outputs and send the result to F3.
      int sum = parallelTasks.Sum(t => t.Result);
      await context.CallActivityAsync("F3", sum);
  }
  ```

- **Async HTTP APIs**
  - addresses problem of coordinating long running operations with external clients
  - HTTP endpoint triggers long running transaction
  - client redirected to a status endpoint that is polled for completion
  - **built in support** in durable functions
  - After instance starts, the extension exposes webhook HTTP APIs that query the orchestrator
  - `HttpStart` triggered function to start instances of orchestrator
  - `DurableClient` input binding *required* for function to interact with orchestrator

  ![Async HTTP APIs](../../Images/async-http-api.png)

  - Code Example (query orchestrator for status)

  ```bash
  > curl -X POST https://myfunc.azurewebsites.net/orchestrators/DoWork -H "Content-Length: 0" -i
  HTTP/1.1 202 Accepted
  Content-Type: application/json
  Location: https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/b79baf67f717453ca9e86c5da21e03ec

  {"id":"b79baf67f717453ca9e86c5da21e03ec", ...}

  > curl https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/b79baf67f717453ca9e86c5da21e03ec -i
  HTTP/1.1 202 Accepted
  Content-Type: application/json
  Location: https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/b79baf67f717453ca9e86c5da21e03ec

  {"runtimeStatus":"Running","lastUpdatedTime":"2019-03-16T21:20:47Z", ...}

  > curl https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/b79baf67f717453ca9e86c5da21e03ec -i
  HTTP/1.1 200 OK
  Content-Length: 175
  Content-Type: application/json

  {"runtimeStatus":"Completed","lastUpdatedTime":"2019-03-16T21:20:57Z", ...}
  ```

  - Code Example (Self Implement pattern)

  ```C#
  public static class HttpStart
  {
      [FunctionName("HttpStart")]
      public static async Task<HttpResponseMessage> Run(
          [HttpTrigger(AuthorizationLevel.Function, methods: "post", Route = "orchestrators/{functionName}")] HttpRequestMessage req,
          [DurableClient] IDurableClient starter,
          string functionName,
          ILogger log)
      {
          // Function input comes from the request content.
          object eventData = await req.Content.ReadAsAsync<object>();
          string instanceId = await starter.StartNewAsync(functionName, eventData);

          log.LogInformation($"Started orchestration with ID = '{instanceId}'.");

          return starter.CreateCheckStatusResponse(req, instanceId);
      }
  }
  ```

- **Monitor**
  - Flexible recurring process in a workflow
  - e.g. polling until specific conditions are met
  - monitors can observe arbitrary endpoints on a timer
  - change the monitor `wait` interval based on condition
  - Code Example

  ```C#
  [FunctionName("MonitorJobStatus")]
  public static async Task Run(
      [OrchestrationTrigger] IDurableOrchestrationContext context)
  {
      int jobId = context.GetInput<int>();
      int pollingInterval = GetPollingInterval();
      DateTime expiryTime = GetExpiryTime();

      while (context.CurrentUtcDateTime < expiryTime)
      {
          var jobStatus = await context.CallActivityAsync<string>("GetJobStatus", jobId);
          if (jobStatus == "Completed")
          {
              // Perform an action when a condition is met.
              await context.CallActivityAsync("SendAlert", machineId);
              break;
          }

          // Orchestration sleeps until this time.
          var nextCheck = context.CurrentUtcDateTime.AddSeconds(pollingInterval);
          await context.CreateTimer(nextCheck, CancellationToken.None);
      }

      // Perform more work here, or let the orchestration end.
  }
  ```

- **Human Interaction**
  - Add a human (approver) in the loop if necessary
  - Code Example (approval with timeout)

  ```C#
  [FunctionName("ApprovalWorkflow")]
  public static async Task Run(
      [OrchestrationTrigger] IDurableOrchestrationContext context)
  {
      await context.CallActivityAsync("RequestApproval", null);
      using (var timeoutCts = new CancellationTokenSource())
      {
          DateTime dueTime = context.CurrentUtcDateTime.AddHours(72);
          Task durableTimeout = context.CreateTimer(dueTime, timeoutCts.Token);

          Task<bool> approvalEvent = context.WaitForExternalEvent<bool>("ApprovalEvent");
          if (approvalEvent == await Task.WhenAny(approvalEvent, durableTimeout))
          {
              timeoutCts.Cancel();
              await context.CallActivityAsync("ProcessApproval", approvalEvent.Result);
          }
          else
          {
              await context.CallActivityAsync("Escalate", null);
          }
      }
  }
  ```

#### Four Function Types

Currentlly four durable function types in Azure. Orchestrator, Activity, Entity, and Client.

- **Orchestrator**
  - Describe how actions are executed and the order of actions
  - Orchestrator functions must be deterministic (must return some input)
  - Orchestrator functions should not be asymc
- **Activity Functions**
  - Basic unit of work in durable function orch
  - Separate tasks in an orchestration are activity functions
  - Not restricted in type of work they can perform
  - Activity functions can onlly have a single value passed (or tuple / array / complex type)
  - `DurableActivityContext` is received as parameter (.Net)
  - `context.bindings.<trigger_name>` used to access input (JavaScript)
- **Entity Function**
  - Define operations for reading / updating pieces of state (*durable entities*) by managing state explicitly
  - *entity trigger* used to trigger
  - No special code constraints
  - *entity ID* used as unique identifier to access entity instance
  - Operations require **Entity ID** and **Operation Name**
- **Client Function**
  - A function is a client function due to use of *durable client output binding*
  - Can be used to trigger other function types that can't be triggered directly (orchestrator / entity)
    - Setup a client function with a *manual trigger* from the azure portal
    - Wire the Client function to trigger the appropraite orchestrator / entity function
    - fire at will (useful for testing)
  - Any *non-orchestrator function*

#### Task Hubs

> To be continued...   https://docs.microsoft.com/en-us/learn/modules/implement-durable-functions/4-durable-functions-task-hubs

#### Resources - Azure Durable Functions

- [Implement Durable Functions (Module)](https://docs.microsoft.com/en-us/learn/modules/implement-durable-functions/)
- [Create a Long Running Serverless Workflow with Durable Functions(Module)](https://docs.microsoft.com/en-us/learn/modules/create-long-running-serverless-workflow-with-durable-functions/)
- [What are Durable Functions?](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview)
- [Create your first durable function in C#](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-create-first-csharp)
- [Durable Functions V1 vs V2](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-versions)
- [Orchestrator Functions Constraints](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-code-constraints?tabs=csharp)
  
## 2 Develop for Azure Storage (15-20%)

## 2.1 Develop Solutions that Use Cosmos DB Storage

### *Select the Appropriate API and SDK for a Solution*

### *Implement Partitioning Schemes and Partition Keys*

### *Perform Operations on Data and Cosmos DB Containers*

#### Resources - Perform Operations on Cosmos DB

- [Quickstart: Azure Cosmos DB SQL API client library for .NET](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/quickstart-dotnet?tabs=azure-cli%2Cwindows)
- [Azure Cosmos DB Resouree Model](https://docs.microsoft.com/en-us/azure/cosmos-db/account-databases-containers-items)

### *Set the Appropriate Consistency Level for Operations*

### *Manage Change Feed Notifications*

## 2.2 Develop Solutions thatUse Blob Storage

### *Move Items in Blob Storage Between Storage Accounts or Containers*

### *Set and Retrieve Properties and Metadata*

### *Perform Operations on Data by Using the Appropriate SDK*

### *Implement Storage Policies, Data Archiving, and Retention*

## 3 Implement Azure Security (20-25%)

## 3.1 Implement user authentication and authorization

### *Authenticate and Authorize Users by using the Microsoft Identity Platform*

### *Authenticate and Authorize Users and Apps by using Azure Active Directory*

### *Create and Implement Shared Access Signatures*

### *Implement Solutions with Microsoft Graph*

## 3.2 Implement secure cloud solutions

### *Secure App Configuration Data by Using App Configuration or Azure Key Vault*

### *Develop Code that Uses Keys, Secrets, and Certificates Stored in Azure Key Vault*

### *Implement Managed Identities for Azure Resources*

## 4 Monitor, troubleshoot, and optimize Azure solutions (15-20%)

## 4.1 Implement caching for solutions

### *configure cache and expiration policies for Azure Cache for Redis*

### *implement secure and optimized application cache patterns including data sizing, connections, encryption, and expiration*

## 4.2 Troubleshoot solutions by using metrics and log data

### *configure an app or service to use Application Insights*

### *review and analyze metrics and log data*

### *implement Application Insights web tests and alerts*

## 5 Connect to and consume Azure services and third-party services (15-20%)

### 5.1 Implement API Management

### *create an APIM instance*

### *create and document APIs*

### *configure authentication for APIs*

### *define policies for APIs*

### 5.2 Develop event-based solutions

### *implement solutions that use Azure Event Grid*

### *implement solutions that use Azure Event Hub*

### 5.3 Develop message-based solutions

### *implement solutions that use Azure Service Bus*

### *implement solutions that use Azure Queue Storage queues*
