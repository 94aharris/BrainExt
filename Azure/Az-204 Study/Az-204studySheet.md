# AZ-204

## 0.0 Resources
- [AZ-204 Exam Information](https://docs.microsoft.com/en-us/learn/certifications/exams/az-204)
- [Thomas Maurer AZ-204 Study Guide](https://www.thomasmaurer.ch/2020/03/az-204-study-guide-developing-solutions-for-microsoft-azure/)
- [Whizlabs AZ-204 Practice Exam](https://www.whizlabs.com/microsoft-azure-certification-az-204/)

## 1 - Develop Azure Compute Solutions (25-30%)

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

- **Azure CLI Commands**
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
  - Other Stuff
    - Enable Registry Admin account (EXPLORATION ONLY)
    ```bash
    az acr update --name <acr_Name> --admin-enabled true
    ```
    - Retrieve username and password for admin account
    ```bash
    az acr credential show --name <acr_name>
    ```
- **Important Tips**
  - ACR is a private registry. Images cannot be accessed without authentication
  - Azure service principals are the recommended authentication method. They provide granular access to container images in ACR
  - When geo-replicating, place container registry in each region where images are run
- Overview
  - Azure Container Registry (ACR) is a managed Docker registry service hosted in azure to build, store, and manage images for containers
  - Container images can be pushed and pulled with Container Registry using Docker CLI or Azure CLI
- Process
  - Create a container image docker fileand use ACR to build the image
  - Deploy the images from ACR
- ACR Authentication
  - ACR doesn't support unauthenticated access and requires auth for all operations
  - supports two typed of Identities
    - Azure Active Directory Identities (user and service principals)
    - Admin Account (included with each registry and disabled by default)
- GeoReplicated Images
  - replicate container registry in each region where images run
  - benefits
    - Single registry/image/tag names used accross multiple regions
    - Network-close registry access from regional deployments
    - No additional egress fees, images are pulled from local replicated registry
    - Siungle management of a registry across regions

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

- **Things to remember**
  - Due to YAML's more concise nature, a YAML file is recommended when a deployment includes only container instances (as opposed to ARM)
  - YAML (reccomended) or ARM is requried when deploying a multi-container group. ```az container create``` will is suited only for single container
- **Azure CLI Commands**
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
- Run containerized tasks with restart policies (three different types)
  - Always - Containers in container group always restarted (**default policy**)
  - Never - Containers are never restarted. Run *at most* once
  - OnFailure - Containers are restarted only when the process executed in the container fails (non-zero exit). Run *at least* once.
  - ACI stops containers when application or script exit. When policy is ```Never``` or ```OnFailure``` the container status is set to *Terminated*
- Container Instances Environmental variables
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
- Mount Azure file share in Azure Container Instances (ACI)
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
     - YAML Example (reccomended)
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
### *Enable Diagnostics Logging*
### *Deploy Code to a Web App*
### *Configure Web App Settings Including SSL, API Settings, and Connection Strings*
### *Implement Autoscaling Rules Including Scheduled Autoscaling and Autoscaling by Operational or System Metrics*

## 1.3 Implement Azure Functions
### *Create and Deploy Azure Function Apps*
### *Implement Input and Output Bindings for a Function*
### *Implement Function Triggers by Using Data Operations, Timers, and Webhooks*
### *Implement Azure Durable Functions*

## 2 Develop for Azure Storage (15-20%)

## 2.1 Develop Solutions that Use Cosmos DB Storage
### *Select the Appropriate API and SDK for a Solution*
### *Implement Partitioning Schemes and Partition Keys*
### *Perform Operations on Data and Cosmos DB Containers*
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
