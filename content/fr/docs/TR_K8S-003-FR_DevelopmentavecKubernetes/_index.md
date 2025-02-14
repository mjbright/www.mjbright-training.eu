---
title: K8S-003-FR Development avec Kubernetes
weight: 1003
---
**Duration: 3 jours**



# Objectifs

L’objectif de cette formation est d’acquérir les bases de l'utilisation et développement d’applications sur Kubernetes, dans le but de:
- Apprendre sur l'orchestration des conteneurs
- Maîtriser la création et hébergement d’images d’applications
- Comment développer les applications en suivant les principes du Cloud Natif
- Connaître les principaux types d’objets gérés par Kubernetes
- Comprendre comment déployer sur Kubernetes
- Savoir déboguer et observer les applications sur Kubernetes
- Comment sécuriser ses applications, Les meilleurs pratiques

La formation serait constituée d'environ 50% théorie et 50% travaux pratiques.

**Note:** Bien que la formation peut-etre une bonne préparation pour l’examen CKAD, elle peut être associée a la formation “K8S-005-FR Preparation a l’examen CKAD”
C’est une journée dédiée aux compétences nécessaires pour réussir la certification.
Nous conseillons de faire une pause entre les deux formations.

Acquis à l'issue de la formation
Le participant à cette formation aura acquis des bases pour administrer une plateforme Kubernetes, en particulier:
- Comment créer des images de conteneurs pour les applications
- Comment héberger des images de conteneurs
- Comment déployer et mettre à jour des applications sur Kubernetes
- Comment exposer des applications
- Déploiement des volumes de données externes
- Observation, Débogage d’applications


# Public concerné et pré-requis

Cette formation vise des ingénieurs qui débutent avec le développement d’applications pour Kubernetes.
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

Proposé sur 3 jours, mais peut-être étendu a 4 jours avoir plus de temps pour les travaux pratiques et ainsi mieux assimiler les concepts et la pratique.
A partir d’un exemple concret, nous regarderons les aspects suivants

**Module: Principes et Concepts de Kubernetes**

- Reprise de principes de Conteneurs
- Pourquoi les Pods - comparaison avec les conteneurs ?
- Lancer et Interagir avec un Pod (ports, exec, logs)
- Résilience à l'échelle “a la Kubernetes”
- Principes de bases: couplage faibles, état désiré, Namespaces, Pods, Controllers, Services
- Installation d’un cluster Kubernetes (kubeadm) et CNI (Cilium)
- Le modele reseau
- Kubeconfig
- Processus de boot, static pods


**Module: Déploiement d’applications avec kubernetes**

- L’architecture
- Pods - init container, multi-container patterns
- Gestion de ressources par Container, par Namespace
- API Kubernetes - API groups, explain, accés API
- Workload controllers
- Mise à jour d’applications
- Stockage: basic, par PV/PVC, dynamic
- ConfigMaps: creation, utilisation, mise à jour
- Secrets: création, utilisation, mise à jour
- Installation et paquetage d’applications avec Helm


**Module: Exposer des applications, Observabilité, Débogage, Sécurité**

- Exposer des applications
  - Services
  - Ingress controller
  - Gateway API
- Observabilité
  - MetricsServer
  - Logging
  - Prometheus/grafana
- Débogage
  - Application troubleshooting avec challenge
- Securite
  - SecurityContext & PodSecurityStandard
  - APIServer controles - Authentication, Authorisation, Admission Control
  - Networkpolicies
- Conseils pour l’examen CKAD|


