---
title: K8S-011-FR Introduction a Helm
weight: 1011
---
**Durée: 1 jour**



# Objectifs

L'objectif de cette formation est de permettre aux participants d'acquérir les bases de l'utilisation de l'outil Helm pour créer et installer des Charts d'applications sous Kubernetes. Les principaux objectifs sont les suivants :
- Faciliter la gestion d’applications sur Kubernetes
- Personnaliser les applications au moment de leur installation

La formation est équilibrée entre la théorie (50%) et les travaux pratiques (50%).

Acquis à l'issue de la formation
À la fin de la formation, les participants auront acquis des compétences pour administrer les applications sur une plateforme Kubernetes en utilisant Helm, notamment :
- Installation, configuration, mise à jour d’une application Kubernetes
- Création et test d’un chart Helm

# Public concerné et pré-requis

Cette formation vise des ingénieurs qui ont déjà une première expérience de développement d’applications pour et utilisation d’un cluster Kubernetes.

Les participants doivent venir avec leur propre PC et avoir accès à Internet:
- via un navigateur pour se connecter à des sites hébergés chez AWS
- ainsi qu'à des VMs EC2 hébergées chez AWS par SSH: moyens de connexion alternatifs peuvent être fourni
Pour tirer pleinement parti de cette formation, les participants:
- doivent être à l'aise pour travailler avec la ligne de commande
- avoir de notions de processus Linux
- avoir de notions de conteneurs et Docker
- Disposer d’un client SSH tel que le client openssh sur Linux, macOS, WSL ou Putty sur Windows

En cas de manquement il est conseillé de d’abord suivre la formation “LIN-001-FR - Introduction a Linux - en ligne de commande / shell” ou equivalent.


# Evaluation

En début de formation, nous vérifions l'expérience dans la domaine ainsi que les attentes de chaque participant.
Si en mode Qualiopi:
En début de formation, une auto évaluation est effectuée pour évaluer le niveau, ainsi que les attentes de chaque participant. Ainsi nous pouvons organiser au mieux les différents groupes de travail.
Le formateur effectue ensuite une évaluation continue à l'aide d'exercices pratiques.

À la fin de la formation, les participants auto-évaluent leur progression, et le formateur fournit une évaluation ainsi que des axes d'amélioration.
En option, un accompagnement post-formation peut être proposé, faisant l'objet d'un devis complémentaire.


# Programme

A partir d’un exemple concret, nous regarderons les aspects suivants

**Module: Introduction à Helm & Concepts de base**

- Présentation de Helm : Qu'est-ce que c'est et pourquoi l'utiliser?
- Comparaison de Helm Charts avec les alternatifs (k8s yaml, kustomize)
- Charts : Structure et composition
- Helm Repositories : ArtifactHub, Chart Museum, Repositories
- Comment installer une application avec Helm

**TP: Installation**

- Creation de cluster Kubernetes via script simplifié
- Installation de Helm
- Recherche d'un Repo & d'un Chart via l’ArtifactHub et le CLI Helm
- Installation du Chart sur un cluster Kubernetes

**Module: Helm Commands et Workflow**

- Structure d'un Chart
- Commandes Helm : helm install, helm upgrade, helm rollback
- Utilisation de valeurs pour personnaliser les installations
- Mise à jour d’une application
- Fonctions de template, variables, conditionnels

**TP: Création d'un Chart simple**

- Récupération d’un chart pour examiner sa structure
- Création d'une structure de base de Chart.
- Installation personnalisé d’un Chart avec l’option ‘--set’
- Installation personnalisé d’un Chart avec ‘-f values.yaml’
- Utilisant de l’option dry-run

**Module: Helm Advanced**

- Mise à jour d’une application
- Quelques commandes helm bien utiles
- Meilleurs Pratiques de Helm
- Utilisation des hooks pre-/post-operation
- Tests de Charts
- Emballage et dépendances

**TP: Mise à jour et Rollback**

- Gestion des releases avec Helm.
- Mise à jour d'un Chart avec de nouvelles valeurs.
- Exécution de rollbacks pour revenir à une version précédente.
- Tests des Charts

**Module: Questions et Réponses, Feedback**

- Répondre aux questions des participants.
- Recueillir des commentaires pour améliorer la formation.|

Terraform
