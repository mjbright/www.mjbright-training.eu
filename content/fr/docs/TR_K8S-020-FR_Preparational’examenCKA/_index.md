---
title: K8S-020-FR Preparation a l’examen CKA
weight: 1020
---
**Durée: 1 jour**



# Objectifs

L’objectif de cette formation d’une journée est de préparer pour passer l’examen “CKA - Certified Kubernetes Administrator” de la Linux Foundation.

Les stagiaires doivent déjà maîtriser la théorie et la pratique de Kubernetes - ayant suivi le “K8S-002-FR Administration Kubernetes” par exemple ou équivalent.

Les stagiaires seraient mis en situation avec des tâches à accomplir - voir plus bas pour plus de détails.

La formation serait constituée principalement (90%) travaux pratiques.

Acquis à l'issue de la formation
Le participant à cette formation serait en bon mesure de passer la certification

# Public concerné et pré-requis

Cette formation vise des ingénieurs qui ont déjà une première expérience d’administration de Kubernetes.
**Note:** De suivre K8S-002-FR et K8S-004-FR seule n’est pas suffisant pour passer l’examen - il faut pratiquer.  Nous fournissons des astuces, la pratique et des ressources pour bien préparer la certification.
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

# Programme

Au longue de la journée, les stagiaires serait mise en situation avec des tâches à accomplir - similaire à ceux rencontrés en examen - du genre
- Implémenter un scénario
  - Un déploiement ou les Pods accède à un ConfigMap monté en Volume
  - Un DaemonSet ou les Pods accède à un Secret par des variables d'environnement
  - Empêcher des Pods en Namespace ‘frontend’ à communiquer directement avec des Pods du Namespace ‘backend’
- Déboguer des scénarios
  - un Service qui ne répond pas aux requêtes, ou de façon intermittent
  - Un Pod qui ne démarre pas, ou un Conteneur qui redemarre sans cesse
  - kubectl qui fait timeout|


