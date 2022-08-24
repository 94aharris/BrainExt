# Security Issues to Look For

## Scoring Tips

- In the portal we only have **READ** access, all changes **Must** come through Azure DevOps
- Target More Critical Vulnerabilities First
- Document Other Vulnerabilities For Later
- Scoring = (# of fixed vulns) * (severity of vuln) ... go for low hanging fruit

## Azure DevOps / Repository

- Project Permissions
  - Do old team members have rights to project
  - Are permissions to high?
- Build Agent Permissions
  - Is the build agent locked down
  - Is the pool locked down from malicious build agents
- Repository Permissions
- Do pull requests to main require a second approver
- Are Commits Verbose
- Are Commits Mapped to Work Items
- Are secrets stored in the repository

## CI/CD Pipelines

- Are variables stored appropriately
- Are secrets passed securely (securestring)
- Are secrets stored in Key Vault
- Are secrets hardcoded in the codebase
- Does the pipeline have access to the production key vault
- Do service principals have separation of duties
- Are Pipelines using Code Scanning
- Are Pipelines using Automated Deployment Testing
  - Unit Tests
  - Regression Tests
  - Integration Tests
  - Load Testing
- Are all deployment stages using the same artifacts
- Are there 4 stage deployments
  - Dev
  - Test
  - Staging
  - Prod
- Do Prod Pipelines require 2 person approval

## Application Infrastructure

- Do Scripts perform input validation
- Are secure inputs passed in correctly (secure strings)
- Are secrets clearned from memory once no longer needed
- Are name length requirements checked
- Are Secrets, Keys, or SAS tokens hard coded
- Are Resources appropriately tagged
- Is there dead code that can be removed
- Are infra components configured to use HTTPS > HTTP
- Are App Gateway's and Web Application Firewalls (WAF) Configured
  - Ensure the Build Agent can still reach the application
- Are Network Security Groups (NSGs) Configured
  - Do not over rely on them
  - Performing filterning at WAF Level
- Are Network Security Groups Configured
- Do Keys Expire and have a Rotation Policy
- Are private resources locked down with service endpoints / private endpoints
  - Ensure build agent can still reach these
- Are Route Tables configured so app sends outbound traffic through Firewalls
- Are Azure Policies configured to enforce security on resources

## Application Encryption

- Is Data in Transit Secure
- Is Data at Rest Secure
- Are Key Vault Keys automatically rotated

## Application Availability

- Is Critical Data Backed Up
- Can the App be redeployed via pipeline
- Are HA Infrastructure components utilized (ILB, AppGateway, etc.)
- Is there a HA/DR Strategy

## Application Reconnaissance Security

- Are Application Powered By Headers Disabled
- Are Verbose Error Pages Disabled

## Application Code Security

- Is Input Validation Performed
  - Front End Input Validation for Users
  - Backend Validation for Attackers
  - SQL Validation for SQL Injection
- Are connections disposed of when no longer needed (Connection Leaks)
- Are services disposing of objects in memory when no longer needed (Memory Leaks)
- Are package dependencies using updated versions or referencing malicious packages
- Does code follow SOLID principals
- Does the Code Implement AAA
  - Authentication (Who are you)
  - Authorization (Are you permitted)
  - Auditing (Logging what was done)
- Is there appropriate documentation for the app
  - Developer Wiki
  - Code Documentation
  - Api Documentation
