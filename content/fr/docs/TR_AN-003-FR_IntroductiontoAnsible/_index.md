---
title: AN-003-FR Introduction to Ansible
weight: 803
---
**Duration: 3 jours**

Cette formation proposée sous forme de formation de 3 jours, ou 6 demi-journées, offre une introduction complète à la gestion de configuration sous Ansible.


**Note:** Cette formation existe également sous forme de formation de 2 jours « AN-002-EN Introduction à Ansible » excluant les modules “Ansible Vault” et “Network Automation”.


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
- Ansible Galaxy Roles


**Module: Optimisation**

- Types de Connection
- Delegation
- Parallelisme
- Callback Plugins


**TP**

- Optimization d’Ansible


**Module: Secrets with Ansible Vault**

- Configuration Vault
- Vault IDs
- Utilisation de Vault


**TP**

- Ansible Vault


**Module: Network Automation**

- Exemples Simple de Module Reseau
- Debogage de Modules Reseaux
- Modules ios
- Exemple de Modules Simple IOS|

WebAssembly
TBD: Introduction to WebAssembly
From ChatGPT:
Jour 1: Introduction à WebAssembly (8 heures)

**Module: C'est quoi WebAssembly? (1 heure)**

Définition de WebAssembly (WASM)
Historique du développement de WASM
Enjeux liés à l'utilisation de WASM
Avantages de WebAssembly


**Module: Cloud Natif et WebAssembly (1 heure)**

Introduction au cloud natif
Intégration de WebAssembly dans les architectures cloud natives
Exemples d'entreprises utilisant WASM dans des environnements cloud


**Module: Overview de la Technologie (2 heures)**

Gestion de la mémoire dans WebAssembly
Isolation des exécutions
Utilisations en navigateur
Utilisations en ligne de commande
Cas d'usage variés de WebAssembly


**Module: Travaux Pratiques (2 heures)**

Mise en place de l'environnement de développement WASM
Exécution de premiers programmes WASM
Exploration des outils de développement et des compilateurs

Jour 2: Modules WASM, Réseau et Outils (8 heures)

**Module: Les Modules WebAssembly (2 heures)**

Comprendre la structure des modules WASM
Interaction avec les modules depuis d'autres langages
Développement de modules WASM personnalisés


**Module: Le Réseau et WebAssembly (2 heures)**

Utilisation de WebAssembly dans le contexte réseau
Exemples de communication entre modules WASM
Cas d'usage spécifiques liés au réseau


**Module: Outils et Runtimes pour WebAssembly (2 heures)**

Exploration de wasmtime et d'autres runtimes
Différents compilateurs pour WebAssembly
Utilisation de WASI, WASIX, et WASI Preview2


**Module: Travaux Pratiques (2 heures)**

Utilisation des outils et runtimes présentés
Expérimentation avec les différentes options de compilation
Manipulation de modules WASM dans des environnements de test


**Module: Bonus: Avancées et Futur de WebAssembly (1 heure)**

Observabilité avec wasmedge et observesdk
Utilisation de WebAssembly avec Docker, HashiCorp Nomad, Kubernetes, Fermyon Spin, Envoy et Open Policy Agent
Perspectives sur l'avenir de WebAssembly


**Module: Conclusion et Questions (1 heure)**

Récapitulation des points clés
Réponses aux questions des participants
Remise de ressources supplémentaires pour approfondir les connaissances
|


