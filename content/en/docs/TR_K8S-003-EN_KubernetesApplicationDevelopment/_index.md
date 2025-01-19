---
title: K8S-003-EN Kubernetes Application Development
weight: 1003
---
# Kubernetes Application Development
**Duration: 3 days**



# Objectives

The objective of the training is to acquire basic skills of Application Development for Kubernetes:
  - Learn about container orchestration
  - Master the creation and hosting of application container images
  - Learn to develop applications following Cloud Native Principles
  - Know the principle types of objects managed by Kubernetes
  - Know how to deploy applications on Kubernetes
  - Be able to debug and observe applications on Kubernetes
  - How to secure applications, best practices
  - The training consists of about 50% theory and 50% hands-on labs.

**Note:** Although the training is a good preparation for the CKAD certification, it can also be combined with the “K8S-005-EN CKAD Exam Preparation” training.
This day is dedicated to practical exercises to help pass the certification.
It is recommended to take the preparation training a week later to properly fix the learnings.


# Training Outcomes

The training participant will acquire basics of Application Developement for Kubernetes, in particular:
  - How to create container images for applications
  - How to host container images in a registry
  - Deploying and upgrading applications on Kubernetes
  - How to expose applications
  - Use of external data volumes
  - Observation, debugging of applications
  - Security & Best practices


# Target Audience

This training is ideal for engineers with little or no experience with Kubernetes application development.
Participants must provide their own PC with internet access, with the ability:
  - to use a browser to connect to sites hosted on AWS
  - to connect to AWS EC2 VMs using SSH
  - (an alternative connection method can be provided)


# Pre-requisites

To take full advantage of this training, participants:
  - should be at ease working at the command line
  - have basic notions of Linux processes
  - have basic notions of container engines such as Docker
  - Be able to use an SSH client such as openssh on Linux, macOS, WSL or Putty on Windows

If lacking command-line skills it is advised to first follow the training “LIN-001-EN - Introduction a Linux - en ligne de commande / shell” or equivalent.


# Evaluation

At the beginning of the training we will verify the domain experience, if any, and any expectations of each participant.
An accompaniment can be proposed at extra cost after the formation.


# Programme

Proposed as a 3 day training, this may be extended to 4 days to have more time to complete the hands-on labs and thus better assimilate the concepts & practical skills.

Working from concrete examples, the following aspects will be covered

**Day 1 : Kubernetes Principles & Concepts**:
  - Review of container principles
  - Why Pods - comparison with Containers, VMs ?
  - Launch and interact with a Pod (ports, exec, logs)
  - “Reliability at scale” with Kubernetes
  - Basic principles: loose coupling, desired state, namespaces, Pods, Controllers, Services
  - Scripted installation of a Kubernetes cluster (kubeadm) & CNI (Cilium)
  - The Kubernetes network model
  - Kubeconfig
  - The Kubernetes bootstrap process, static Pods


**Day 2 : Deploying applications on Kubernetes**:
  - Kubernetes architecture
  - Pods - init containers, multi-container patterns
  - Resource management by Container, by Namespace
  - API Kubernetes - API groups, explain, API access
  - Workload controllers
  - Application upgrades
  - Storage: basic, PV/PVC, dynamic provisioners
  - ConfigMaps: creation, usage, updating
  - Secrets: creation, usage, updating
  - Installing applications with Helm


**Day 3 : Exposing applications on Kubernetes, Observability, Debugging, Sécurity**:
Exposing applications:
    - Services
    - Ingress controller
    - Gateway API
Observability:
      - MetricsServer
      - Logging - EFK, Loki
      - Metrics - Prometheus/grafana
Troubleshooting:
        - Application troubleshooting with challenge
Security:
          - SecurityContext & PodSecurityStandard
          - APIServer stages - Authentication, Authorisation, Admission Control
          - Policy Engines: OPA, Kyverno
          - Networkpolicies
          - Advice for taking the CKAD exam|


