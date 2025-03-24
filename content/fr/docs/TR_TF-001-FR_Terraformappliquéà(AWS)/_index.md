---
title: TF-001-FR Terraform appliqué à (AWS)
weight: 901
---
**Durée: 1 jour**

Cette formation proposée en formation d'1 journée, ou 2 demi-journées, applique au Cloud AWS les principes de Terraform déjà appris dans la formation « TF-000-EN Terraform Introduction (CORE) » de 2 jours aux ressources.


Cette formation sera davantage orientée vers la pratique que vers la théorie : elle n'est pas destinée à enseigner AWS, mais à expérimenter l'application de Terraform aux ressources AWS.


**Note:** Suivre « TF-000-FR Terraform Introduction (CORE) » est un prérequis pour cette formation spécifique au cloud.


Terraform permet de gérer le déploiement de différents types d'infrastructures via le plugin « Provider » approprié - ce cours utilise le fournisseur AWS permettant de gérer de nombreuses ressources cloud AWS.


Les étudiants apprécieront la facilité avec laquelle les ressources d'infrastructure sont définies de manière déclarative permettant de créer, de mettre à jour ou de détruire des ressources de manière idempotente.


Terraform utilise HCL v2 – « HashiCorp Configuration Language » – pour définir les ressources à créer pour 1 ou plusieurs fournisseurs.


**Note:**  le même cours est disponible pour d'autres fournisseurs|

# Pre-requisites

- Soyez à l'aise en travaillant en ligne de commande et en éditant des fichiers
- Notions de base de Cloud, Linux, Conteneurs
- Utilisation d'un client ssh, par ex. openssh sous Linux, macOS ou Windows (ou Putty)|

# Compris

- Supports de cours et laboratoires : 50 % de travaux pratiques, 50 % de présentation et de démonstrations
- Accès à un environnement de laboratoire temporaire
- Accès à un document évolutif couvrant diverses ressources d'apprentissage Terraform
|

# Objectives

- Apprenez à utiliser Terraform pour mettre en place diverses ressources AWS, de manière déclarative
- Apprenez à utiliser les modules, sources de données et outils spécifiques à AWS
|

**Note:** les ressources spécifiques AWS suivantes sont proposées, mais peuvent être adaptées aux besoins des clients.


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

