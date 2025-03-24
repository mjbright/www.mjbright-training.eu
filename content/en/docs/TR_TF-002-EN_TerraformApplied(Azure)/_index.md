---
title: TF-002-EN Terraform Applied (Azure)
weight: 902
---
**Duration: 1 day**

This training proposed as a 1-day training, or 2 half-days, applies to the Azure Cloud the principles of Terraform already learnt in the “TF-000-EN Terraform Introduction (CORE)” 2-day training to resources.

This training will be oriented more toward hands-on than theory - it is not intended to teach about Azure, but to experience the application of Terraform to Azure resources

**Note:** Taking “TF-000-EN Terraform Introduction (CORE)” is a prerequisite for this cloud specific training.

Terraform allows to manage the deployment of different infrastructure types via the appropriate “Provider” plugin - this course uses the Azure provider allowing to manage many Azure cloud resources.

Students will appreciate the ease with which infrastructure resources are defined in a declarative manner allowing resources to be created, updated or destroyed in an idempotent manner.

Terraform uses HCL v2 - “HashiCorp Configuration Language” - to define resources to be created for 1 or more providers.

**Note:** the same course is available for other Providers|

# Pre-requisites

Be at ease working at the command-line, editing files
Basic notions of Cloud, Linux, Containers
Use of an ssh Client, e.g. openssh on Linux, macOS or Windows (or Putty)
|

# Included

Course materials and labs: 50% hands-on, 50% presentation & demos
Access to a temporary lab environment
Access to an evolutive document covering various Terraform learning resources
|

# Objectives

Learn to use Terraform for standing up various Azure resources, in a declarative manner
Learn to use Azure specific modules, data sources & tooling
|
**Note:** the following Azure specific resources are proposed, but can be adapted to customer needs


# Programme


**Module: Review**

- Infrastructure as Code principles
- Terraform & OpenTofu workflows


**Module: Working with Containers**

- Managing Azure ACI containers with Terraform
- Using Data Sources with Azure ACI


**Module: Working with VMs**

- Managing Azure virtual machines with Terraform
- Using Data Sources with Azure VMs


**Module: Working with modules**

- Terraform registry:: Working with existing terraform modules for Azure
- Writing modules for Azure: Creating clusters of VMs


**Module: Templates**

- Creating useful templates (ssh_config, ansible inventory, reports)


**Module: In Practice**

- Variable validation
- Debugging
- 3rd-party tools


**Module: State**

- Local State
- Using Azure Blob Storage for “remote state”


**Module: Importation of foreign ressources**

- Importation of Azure resources
- Move of Azure resources


**Module: Auto-scaling & Load-Balancing**

- Azure VM ScaleSets
- terraform-azurerm-loadbalancer


**Module: Other Azure resources**

- Azure functions, Azure VPC, Azure Public IP, Blob Storage, AKS


**Module: In Production**

- Provisioners (Local-exec, File, Remote-exec)
- Provider Aliases|

