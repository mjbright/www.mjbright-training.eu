---
title: TF-000-FR Introduction a Terraform (CORE)
weight: 900
---
**Duration: 2 jours**

Cette formation, proposée sous forme de formation de 2 jours, ou 4 demi-journées, présente aux étudiants les avantages de développer « Infrastructure as Code » avec Terraform.


L'intention est de suivre cette formation de 2 jours par une formation distincte d'une journée qui applique les concepts appris au fournisseur de cloud préféré du client (AWS, Azure, Google Cloud, Oracle) ou à un autre environnement virtualisé (Proxmox, OpenStack).


**Note:** Ces formations sont proposées sous forme de Terraform, mais peuvent également être dispensées sous forme de formations OpenTofu.


Cette formation initiale de 2 jours est la manière recommandée pour apprendre les bases de Terraform :
- Il utilise principalement Docker ou des Providers locaux pour les exercices de base - Cela permet d'assimiler les concepts Terraform importants à un rythme accéléré


Terraform permet de gérer le déploiement de différents types d'infrastructures via le plugin « Provider » approprié - ce cours utilise le fournisseur Docker pour pouvoir expérimenter dix fois plus rapidement qu'en utilisant des Cloud Providers ou même des Hyperviseurs.


Les étudiants apprécieront la facilité avec laquelle les ressources d'infrastructure sont définies de manière déclarative - en utilisant HCL v2 - « HashiCorp Configuration Language » - permettant de créer, mettre à jour ou détruire des ressources de manière idempotente.


Il est recommandé de combiner cette formation de 2 jours avec une ou plusieurs des formations d'une journée spécifiques au prestataire suivantes :
- TF-001-FR Terraform Introduction (AWS)
- TF-002-FR Terraform Introduction Terraform (Azure)
- TF-003-FR Terraform Introduction Terraform (Google Cloud)
- TF-004-FR Terraform Introduction Terraform (Oracle Cloud)
- TF-005-FR Terraform Introduction Terraform (OpenStack)
- TF-006-FR Terraform Introduction Terraform (Proxmox)|

# Pre-requisites

- Soyez à l'aise en travaillant en ligne de commande et en éditant des fichiers
- Notions de base de Cloud, Linux, Conteneurs
- Utilisation d'un client ssh, par ex. openssh sous Linux, macOS ou Windows (ou Putty)|

# Included

- Supports de cours et laboratoires : 50 % de travaux pratiques, 50 % de présentation et de démonstrations
- Accès à un environnement de laboratoire temporaire
- Accès à un document évolutif couvrant diverses ressources d'apprentissage Terraform|

# Objectives

- Apprenez à utiliser Terraform pour mettre en place diverses ressources, de manière déclarative
- Apprenez les nombreuses subtilités de Terraform/HCLv2 pour écrire des configurations déclaratives de qualité
Sachez où trouver des informations sur les autres fournisseurs, modules pour Google Cloud, Azure etc…|

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
