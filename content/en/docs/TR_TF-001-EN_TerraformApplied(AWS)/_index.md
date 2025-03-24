---
title: TF-001-EN Terraform Applied (AWS)
weight: 901
---
**Duration: 1 day**

This training proposed as a 1-day training, or 2 half-days, applies to the AWS Cloud the principles of Terraform already learnt in the “TF-000-EN Terraform Introduction (CORE)” 2-day training to resources.

This training will be oriented more toward hands-on than theory - it is not intended to teach about AWS, but to experience the application of Terraform to AWS resources

**Note:** Taking “TF-000-EN Terraform Introduction (CORE)” is a prerequisite for this cloud specific training.

Terraform allows to manage the deployment of different infrastructure types via the appropriate “Provider” plugin - this course uses the AWS provider allowing to manage many AWS cloud resources.

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

Learn to use Terraform for standing up various AWS resources, in a declarative manner
Learn to use AWS specific modules, data sources & tooling
|

**Note:** the following AWS specific resources are proposed, but can be adapted to customer needs


# Programme



**Module: Review**

- Infrastructure as Code principles
- Terraform & OpenTofu workflows


**Module: Working with Containers**

- Managing AWS ECS containers with Terraform
- Using Data Sources with AWS ECS


**Module: Working with VMs**

- Managing AWS EC2 virtual machines with Terraform
- Using Data Sources with AWS EC2


**Module: Working with modules**

- Terraform registry: Working with existing terraform modules for AWS
- Writing modules for AWS: Creating clusters of VMs


**Module: Templates**

- Creating useful templates (ssh_config, ansible inventory, reports)


**Module: In Practice**

- Variable validation
- Debugging
- 3rd-party tools


**Module: State**

- Local State
- Using AWS/S3+DynamoDB for “remote state”


**Module: Importation of foreign ressources**

- Importation of AWS resources
- Move of AWS resources


**Module: Auto-scaling & Load-Balancing**

- AWS EC2 ASG - Autoscaling Groups
- AWS EC2 ALB - Application Load Balancer


**Module: Other AWS resources**

- Lambda, VPC, EIP, S3, EBS, IAM, RDS


**Module: In Production**

- Provisioners (Local-exec, File, Remote-exec)
- Provider Aliases|

