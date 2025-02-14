---
title: TF-000-EN Terraform Introduction (CORE)
weight: 900
---
**Duration: 2 days**

This training, proposed as a 2-day training, or 4 half-days, introduces students to the advantages of developing “Infrastructure as Code” with Terraform.

The intention is to follow this 2-day training with a separate 1-day training which applies the concepts learnt to the customers preferred Cloud Provider (AWS, Azure, Google Cloud, Oracle) or other virtualized environment (Proxmox, OpenStack).

**Note:** These trainings are proposed as Terraform, but can equally be delivered as OpenTofu trainings

This initial 2-day training is the recommended way to learn Terraform basics:
- It uses mainly Docker or local Providers for the base exercises - This allows to assimilate important Terraform concepts at an accelerated pace

Terraform allows to manage the deployment of different infrastructure types via the appropriate “Provider” plugin - this course uses the Docker provider to be able to experiment ten times faster than when using Cloud Providers or even Hypervisors.

Students will appreciate the ease with which infrastructure resources are defined in a declarative manner - using HCL v2 - “HashiCorp Configuration Language” - allowing resources to be created, updated or destroyed in an idempotent manner.

It is recommended to combine this 2-day training with one or more of the following 1-day Provider specific trainings:
- TF-001-EN Terraform Introduction (AWS)
- TF-002-EN Terraform Introduction Terraform (Azure)
- TF-003-EN Terraform Introduction Terraform (Google Cloud)
- TF-004-EN Terraform Introduction Terraform (Oracle Cloud)
- TF-005-EN Terraform Introduction Terraform (OpenStack)
- TF-006-EN Terraform Introduction Terraform (Proxmox)
|

# Pre-requisites

- Be at ease working at the command-line, editing files
- Basic notions of Cloud, Linux, Containers
- Use of an ssh Client, e.g. openssh on Linux, macOS or Windows (or Putty)
|

# Included

- Course materials and labs: 50% hands-on, 50% presentation & demos
- Access to a temporary lab environment
- Access to an evolutive document covering various Terraform learning resources
|

# Objectives

- Learn to use Terraform to stand up various resources, in a declarative manner
- Learn the many intricacies of Terraform/HCLv2 to write quality declarative configs
Know where to find information about other Providers, Modules for Google Cloud, Azure etc …
|

# Programme



**Module: Introduction to Infrastructure as Code**

- HashiCorp “free to use” ecosystem
- Infrastructure as Code, Config Management, Idempotence
- Terraform
- Installation


**Module: Terraform Workflow**

- The plan
- Applying and re-applying plans
- Destroying resources
- Various sub-commands


**Module: HCL Configurations**

- Providers
- Variables
- Resources


**Module: Variable types**

- Variables,passing values to the configuration, Locals
- Basic and complex types
- Functions


**Module: Control Structures**

- Count, ternary, for_in, for_each
- Dynamic Blocks
- Templates


**Module: Terraform Registry**

- Provider Data Sources
- Modules
- Using Modules
- Writing your own Modules


**Module: In Practice**

- Variable validation
- Debugging
- 3rd-party tools


**Module: State**

- Local State
- Using “remote state” for working in teams


**Module: Importation of foreign ressources**

Importation of resources created outside Terraform:
- terraform import
- Import blocks


**Module: In Production**

- Provisioners (Local-exec, File, Remote-exec)
- Terraform Best practices
- Tooling: Linters, scanners, testers
- Terraform test


**Module: HashiCorp Terraform Eco-system**

- HCP Terraform & Enterprise
- Terraform CDK
- Waypoint, Boundary
- Terraform Certification
|
