---
title: K8S-002-EN Kubernetes Administration
weight: 1002
---
**Duration: 4 days**

The objective of the training is to acquire Kubernetes Administration basics:
- Learn about container orchestration
- Master the installation, configuration of a Kubernetes platform
- Understand the main types of objects managed by Kubernetes
- Know how to deployer applications on Kubernetes
- Be able to debug and observe applications and the Kubernetes cluster itself

The training consists of about 50% theory and 50% hands-on labs.

**Note:** Although the training is a good preparation for the CKA certification, it can also be combined with the “K8S-004-EN CKA Exam Preparation” training.
This day is dedicated to practical exercises to help pass the certification.
It is recommended to take the preparation training a week later to properly fix the learnings.


# Training Outcomes

The training participant will acquire Kubernetes Administration basics, in particular:
- Installation, Configuration, Upgrading of a Kubernetes Cluster
- Deploying and upgrading applications on Kubernetes
- How to expose applications
- Use of external data volumes
- Observation, debugging of applications & of the cluster
- Security & Best practices


# Target Audience

This training is ideal for engineers with little or no experience with Kubernetes administration.
Participants must provide their own PC with internet access, with the ability:
- to use a browser to connect to sites hosted on AWS
- to connect to AWS EC2 VMs using SSH: alternative connection methods can be provided


# Pre-requisites

To take full advantage of this training, participants:
- should be at ease working at the command line
- have basic notions of Linux processes
- have basic notions of container engines such as Docker
- Be able to use an SSH client such as openssh on Linux, macOS, WSL or Putty on Windows

If lacking command-line skills it is advised to first follow the training “LIN-001-EN - Introduction to Linux - command-line / shell” or equivalent.


# Evaluation

At the beginning of the training we will verify the domain experience, if any, and any expectations of each participant.
An accompaniment can be proposed at extra cost after the formation.


# Programme

Proposed as a 4 day training, this may be extended to 5 days to have more time to complete the hands-on labs and thus better assimilate the concepts & practical skills.

Working from concrete examples, the following aspects will be covered

**Module: Kubernetes Principles & Concepts**

- Review of container principles
- Why Pods - comparison with Containers, VMs ?
- Launch and interact with a Pod (ports, exec, logs)
- “Reliability at scale” with Kubernetes
- Basic principles: loose coupling, desired state, namespaces, Pods, Controllers, Services
- Installation of a Kubernetes cluster (kubeadm) & CNI (Cilium)
- The Kubernetes network model
- Kubeconfig
- The Kubernetes bootstrap process, static Pods


**Module: Deploying applications on Kubernetes**

- Kubernetes architecture
- Pods - init containers, multi-container patterns
- Resource management by Container, by Namespace
- API Kubernetes - API groups, explain, API access
- Workload controllers
- Application upgrades
- Storage: basic, PV/PVC, dynamic provisioners


**Module: More storage, exposing applications on Kubernetes**

- ConfigMaps: creation, usage, updating
- Secrets: creation, usage, updating
- Extending Kubernetes - Helm, CRDs, Operators
- Exposing applications
  - Services
  - Ingress controller
  - Gateway API
- ServiceMesh


**Module: Observability, Debugging, Sécurity, HA**

- Observability
  - MetricsServer, Dashboard
  - Logging - EFK, Loki
  - Metrics - Prometheus/grafana
- Troubleshooting
  - Application troubleshooting with challenge
- Security
  - SecurityContext & PodSecurityStandard
  - APIServer stages - Authentication, Authorisation, Admission Control
  - Policy Engines: OPA, Kyverno
  - Networkpolicies
- Cluster HA
- Advice for taking the CKA exam
|


