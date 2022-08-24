# Azure Security Challenge

## Important Highlights

- Remove x-powered-by headers
- Review security checklist
- Script for basic lockdowns
- Drive decisions with data. Data. DATA
- Don't focus on network boundary. Focus on IDENTITY management. Make sure identity is well controlled and protected.
- Check **Permissions** on objects
- Use Defender for Cloud Apps
- For Global Admins, have PIM requests sent to external groups (Just in time admin access)
- Focus on simple, effective, and top priority security concerns
- Familiarize with TIC 3.0 concepts
- The challenge will primarily be about things you can **See and correct**
  - Things that are done wrong in code
    - Https incorrectly implemented
    - Password in the code
  - Things that are done wrong in configuration
  - Things that are done wrong in permissions
- Are things **encrypted**?
- Divide resources into Dynamic / Static resource groups
  - Dynamic can be blown away and re-deployed
  - Static needs to be persisted (Key Vault, User Data, etc.)

## Outline

- Intro
  - Preparing for Secure Application Deployments
    - project and work item planning, and project configuration
    - Centralized security services in Azure
  - Security CI/CD Pipelines
        variables, builds, and releases
  - Securing Application Infrastructure
    - scripts ARM templates, resource configs
  - Securing Application Code
    - secure coding practices

## Competition Overview

- This will be a pre-done app and you need to secure it
- Extra points for complaining about how the previous team left the app ;-)

## Intro

Testing is the most imporant things you can integrate with your CI/CD pipelines

Things are never so bad that they can't get worse | Your app is never so good that it can't get better

Zero Trust == don't trust something just because it's on your network

DevOps is more work intensive up front, but don't let it cause analysis paralysis (Bias for Action)

## Preparing for Secure Application Deployments

### Cybersec *generally*

- Assume breach
- zero truse
- micro segementation
- tier your appliation

### Avoid security *theater*

- dont rely on obscurity
- dont restrict just to restrict
- avoid burdensome security (drives bad behavior)
- deprioritize low risk threats (spend time on more realistic threats)

### Threat / Vuln Categories

- Intentional (cyberattacks, insiders, sabotage, etc.)
- Natural (Flood, Hurricane, etc.)
- Unintentional (Mistakes, Bad processes, Neglect, Poor design, etc.)

### Domains of Concerns (in order of perimiter to nuget-y center)

- Reconnaissance
  - **Headers (x-powered-by header)**
  - How can we limit the amount of information we expose about our app?
- External Shenanigans
  - DNS Poisoning
  - Compromising external users host files
  - How can we protect users against others attacking them?
- Perimeter Breach
  - Always assume a Perimeter Breach (Zero Trust)
  - What internal perimeters exist within our application?
  - Where is the border for our application?
- Systems Compromise
  - Web Tier, App Tier, etc.
  - What happens if an individual system is compromised?
- Data Compromise
  - Key Vault w/ Storage Account and automatic key rotation
  - Are we encrypting data at rest?

### Security Services at a Glance

- Monitoring and Logging
  - **Application Insights** should be used by every app
  - Defender for Cloud
  - Sentinal (more for central security team)
    - Draws data from one or more log analytics workspaces
    - Recc. Have one instance of Sentinal and put all Log analytics workspaces there
  - Log Analytics
  - Alerts
  - Network Watcher
- Security
  - **App Gateway w/ Waf** - important
  - **Managed Identities** - important
  - Front Door
  - MCAS -> acts as an SSL Termination Proxy
- Privacy
  - Private Endpoint
    - Requires DNS services in Azure and On-Premise DNS Forwarder
    - Lots of organizational coordination req
    - Works for services / vms only in Azure -> better to use Service Endpoint in this case
  - Service Endpoint
  - Private Link
- Centralized Security
  - MOAR Defender -> Defender for Cloud & Microsoft 365 Defender
  - O365 is for office -> M365 is O365 + everything else

### Beware 'turtles all the way down'

Adding layers of substantially the same mitigation is not, in and of itself good security

- Firewall behind an identical firewall behind another identical firewall adds cost and complexity but not additional security
- **Defense in Depth** works best when you add layers of substantially different protections

### Consistency, Complexity, Humanity

Design your apps and security for humans. Be consistent.

> "Any fool can write code a computer can understand. Programmers write code that humans can read" ~ Martin Fowler

### Key Considerations

- Secure handling of **secrets** (key vault)
- Input validation
- Clean and consistent code
- Scanning and testing
  - Sonarqube, Fortify, OWASP
  - Load Testing
  - Testing Pyramid
- Identify controls and zero trust concepts
- CIA Triad
- High Availability and Disaster Recovery
- Encryption
- AuthN & AuthZ
- Minimize public information
  - Headers, Error Pages, etc.
- Avoid security theaters, unnecessary complexity, and turtles

## Designing and Preparing for your App (IMPORTANT FOR COMPETITION)

### Preparing DevOps for Secure Application Deployments

- Configure and secure a DevOps Project **Very Important to Secure**
  - There should only be 2 people that can modify pipelines
  - Set approvers before application is promoted to Prod
  - Three person integrity (help mitigate insider threats)
- Develop application testing plan **This tends to get missed**
- Develop backup and disaster recovery (DR) strategies **This tends to get missed**
- CIA Triad
- Set up backlog to include key security activities **Every Idea for the app, throw it in the backlog**
- **TIC 3.0** and Zero Trust
  - Turn centralized groups into consultant groups
- Centralized Security services in Azure
  - Know what is covered by central services
- Planning to encrypt data at rest (TDE, Column Encryption) and in transit (Https, private blob endpoints)
  - In azure, everything is encrypted at rest with **Microsoft Encryption**
  - To bring **your own** encryption, you need to configure that manually
- Things to look for
  - Permissions
    - Old team members who have rights to project?
    - Permissions are too high for someone?
  - Groups & Teams
  - Build Agents
    - Locked down correctly
    - Agent pool dedicated for high priority apps
    - **Gaurd your pool** from malicious build agent
  - Repository
    - Repo policy and permissions
    - Branch policy
    - Git comment standards
    - Squash Merge
    - **Protect the branches** with pull policies
  - Three person integrity
    - Merge required to be reviewed by second person!!
    - Require Production stage deployment approval by team lead / alternate
  - Develop application testing plan
    - Code scanning
    - Unit tests
    - Integration tests
    - Regression Tests
    - Load tests
  - Automate application tests
  - Map work items to commits

### Application Deployment Availability

- Develop backup and DR strategies
  - Hot/Warm/Cold
  - Regional capabilities
- Backlog Work Items
  - include testing as pre-prod requirements
  - Backup and DR configuration
- Zero Trust
  - TIC 3.0
  - Don't trust the network
  - Robust **Identity Based** security

### Azure Level Security

- Leverage PIM
- Conditional Access
- Configure alerts, auditing, and centralized security tools

## Securing CI/CD Pipelines

### Variables

- Make use of Yaml multi-stage pipelines over Legacy pipelines
  - Add Yaml pipelines into source control
  - Capture variables values in code repository
- Consider likelihood of change

### Secrets

- Pass secrets securely (secure string)
- Pipeline should not be able to access production secrets
  - The Production Key Vault should be open to the Dev Pipeline
  - The Production Build Agent should have access to Prod Keys
- Automate Secret rotation
- Do not store in codebase
- Separate duties via service principals

### Builds and Releases

- Deployment Stages
  - Dev: Does my app work, rapid testing
  - Test: Test with production-like settings / interactions
  - Staging: Push to prod on prod vnet (without endpoint)
  - Production: Update App
- All Deployment Stages should use exact same artifacts
- **Require Prod Stage Approval** by at least two folks
- Use service connections to hold deplyment identity and secrets
- Use Code Scanning
- Use Automated Deployment Testing

### Wrap-Up

- Minimize pipeline variables
- Do not hard-code secrets
- Pass secrets securely
- Delete secrets from memory when not needed
- Use deployment stages (4 optimally)
- Automate testing and continuously update as new issues are found

## Securing Application Infrastructure

### Scripts

- Script Security
  - Input Validation
    - Length
    - data type
    - allowed chars
  - Remove unneeded variables
  - Dead Code
- Regex Patterns for Azure Naming Rules

### ARM Template

- ARM template security
  - parameter input validation
  - Pass secrets securely
  - Do not hard code secrets, keys, or SAS tokens

### Azure Resource Configurations

- Secure Networking
  - Service Endpoints (Inbound Comms)
  - Private Endpoints (Inbound Comms)
  - VNet Integration (Outbound Comms)
  - Network Security Group (Don't over rely on them)
  - Route Table (Ensure web app routes out via Firewall)
- Tagging (POC and office, purpose)
- Choose HTTPS
- App Gateway w/ Web Appliation Firewall (WAF)
  - IP and Subnet Based Rules
- Azure Firewall
  - Be aware, firewall can introduce interesting behavior
  - Route table (UDR) send all traffic to firewall
  - Firewall has policy / service endpoint to ensure that traffic can only go to specific Storage Account
- Load Balancer
  - Allows distributed connections to app
  - Delete and re-create VMs while the app is running
- IAM and Azure Policy

### Key Rotations

- Ensure Keys have Expiration and Rotate Appropriately

### Infrastructure Wrap Up

- Input Validation Critical
- Pass Secrets Securely
  - Clear variable once done using (from memory)
- Use networking controls to secure comms between resources
- Use Office Tags to help security contact

## Securing Application Code

### Secure Coding Practices

- Input Validation
  - Front End
  - Back End
  - Sql Injection
- Connection Leaks
  - Dispose of connections when no longer needed
- Memory Leaks
  - Dispose of object when no longer needed
- Dead Code
- SOLID Principles
  - SRP
  - Open Closed
  - Liskov Substitution
  - Interface Segregation
  - Dependency Injection
- App team agreement on standardizing coding style
- Package libraries with malicious code
- Architectural styles
  - Command Query Responsibility Segregation (CQRS)
  - Model View Controller (MVC)
  - Model View View Model (MVVM)

### Authentiation and Authorization Mechanisms

- AAA
  - Authentication (AuthN) - "Who are you?"
  - Authorization (AuthZ) - "Are you permitted to access"
- Understand tradeoffs between authentication choice (e.g. Kerberos) and specific infrastructure resources (e.g. App Gateway)

### Documents and Documentation

- Documentation for Developers (e.g. Wiki)
- Self Documenting Code

## Summary of Training

- Security, like testing, is *integral* to both dev and ops
- Secure app design is holistic. It must start at project inception and be baked into th backlog and project / pipeline design from the start
- **Availability*8 is part of the CIA triad and just as important. Not all threats are bad actors. Design HA/DR from the start
- Pipelines should be the backup for the app. Only production data should be backed up via other means.
- Opposite of **security** is **complexity**
- Defense in depth but avoid turtles
- Should be useable, usagility trumps individual security
- Consider your budget
- Risk mgmt vs. Risk avoidance vs. risk transference
- Consider cost overrun attacks (throttling limits, alerting, etc.)
