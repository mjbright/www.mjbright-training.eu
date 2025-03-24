---
title: AN-002-FR Introduction to Ansible
weight: 802
---
**Durée: 2 jours**

Cette formation proposée sous forme de formation de 2 jours, ou 4 demi-journées, offre une introduction complète à la gestion de configuration sous Ansible.


**Note:** Cette formation existe également sous forme de formation de 3 jours « AN-003-EN Introduction à Ansible » permettant plus de temps pour les TP et également l'ajout de modules “Ansible Vault” et “Network Automation”.


Cette formation comprend beaucoup de pratique ainsi que de théorie.
Tous les exercices pratiques seront effectués sur des machines virtuelles et des conteneurs Linux.


Les étudiants apprécieront la facilité avec laquelle les logiciels peuvent être installés et maintenus de manière fiable, reproductible et réutilisable au sein des équipes grâce à la nature largement déclarative des Playbooks et rôles Ansible.   Les playbooks peuvent être réexécutés, garantissant des résultats reproductibles en raison de la nature idempotente d'Ansible.|

# Pre-requisites

- Soyez à l'aise en travaillant en ligne de commande et en éditant des fichiers
- Notions de base de Cloud, Linux, Conteneurs
- Utilisation d'un client ssh, par ex. openssh sous Linux, macOS ou Windows (ou Putty)|

# Compris

- Supports de cours et laboratoires : 50 % de travaux pratiques, 50 % de présentation et de démonstrations
- Accès à un environnement de laboratoire temporaire
- accès à un document évolutif regroupant diverses ressources d'apprentissage|

# Objectifs

- Apprenez à utiliser Ansible pour effectuer la configuration logicielle et la maintenance des machines/appareils
- Découvrez les nombreux modules intégrés, collections de modules et rôles pour Ansible
- Découvrez les meilleures pratiques pour travailler avec Ansible|


# Programme



**Module: Introduction**

- Pourquoi Ansible?
- Concepts & Termes
- Agentless Architecture
- Inventory
  - Static & Dynamique
  - Host & Group Patterns


**Module: Deploying with Ansible**

- Installation de Ansible
- Fichiers de configuration YAML
- Playbooks
  - Modules Ansible
  - Commandes Ad-Hoc
  - Inventory Dynamique
    - Scripted
    - Plugins


**TP**

- Deploiement Ansible
- Commandes Ad-Hoc
- Inventories Dynamiques


**Module: Playbooks**

- Structure de Playbook
- Ordre d’execution - Host & Task
- Categories de Modules
  - Command
  - File Manipulation
  - Network Modules
  - Packaging Modules
  - System Storage
  - Account Management
  - Security
  - Services


**TP**

- Playbook Basiques
- Playbooks: Command Modules
- Playbooks: Common Modules


**Module: Variables**

- au runtime
- dans Playbooks
- register task output, debug module
- dans inventory: host_vars, global_vars
- Scope & precedence
- Facts & magic variables
- dans included files, roles
- Output: callback plugins


**TP**

- Variables & Facts
- Inclusions


**Module: Jinja Templating**

- Jinja Expressions
- Builtin.template module
- Filtres
- Methodes
- Conditionels
- Lookup plugins
- Structures de Control


**TP**

- Templates Jinja


**Module: Control Structures**

- Loops & Variables (with)
- Conditionels (when)
- Handlers
- Tags
- Error Handling


**TP**

- Task Control


**Module: Roles**

- Usage
- Creation de Roles
- Deploiement de Roles avec Ansible Galaxy


**TP**

- Conversion Playbooks a Roles
- Creation de Roles from Scratch
- Ansible Galaxy Roles|

