---
title: K8S-011-EN Introduction to Helm
weight: 1011
---
# Introduction to Helm
**Duration: 1 day**



# Objectives

The objective of the training is to acquire basic skills of using Helm to create and install application Charts for Kubernetes.  The principal objectives are :
  - Faciliter application life-cycle management on Kubernetes
  - Customize applications at installation time
  - The training consists of about 50% theory and 50% hands-on labs.


# Training Outcomes

The training participant will acquire the basics of Application life-cycle management using Hem, in particular :
  - Installation, configuration, upgrading of an application on Kubernetes
  - Creation & test of a Helm chart
  - Target Audience
  - This training is ideal for engineers with some experience with Kubernetes application development.
Participants must provide their own PC with internet access, with the ability :
    - to use a browser to connect to sites hosted on AWS
    - to connect to AWS EC2 VMs using SSH
    - (an alternative connection method can be provided)

  - Pre-requisites
To take full advantage of this training, participants :
    - should be at ease working at the command line
    - have basic notions of Linux processes
    - have basic notions of container engines such as Docker
    - Be able to use an SSH client such as openssh on Linux, macOS, WSL or Putty on Windows

  - If lacking command-line skills it is advised to first follow the training “LIN-001-EN - Introduction a Linux - en ligne de commande / shell” or equivalent.


# Evaluation

At the beginning of the training we will verify the domain experience, if any, and any expectations of each participant.
An accompaniment can be proposed at extra cost after the formation.


# Programme

Proposed as a single day training, this may be extended to 2 days to going into more depth and with more time to complete the hands-on labs and thus better assimilate the concepts & practical skills.

Working from concrete examples, the following aspects will be covered
Introduction to Helm & Concepts:
  - Introduction to Helm : What is it, why do we need it ?
  - Comparison of Helm Charts with alternatives (k8s yaml, kustomize)
  - Charts : Structure & composition
  - Helm Repositories : ArtifactHub, Chart Museum, Repositories
  - How to install an application with Helm

TP1 - Installation:
  - Creation of a Kubernetes cluster via a simplified script
  - Helm Installation
  - Searching for a repository and a chart via the ArtifactHub & the Helm CLI
  - Installation of a Chart on a Kubernetes cluster

Helm Commands & Workflow:
  - Chart Structure
  - Helm Commands : helm install, helm upgrade, helm rollback
  - Customizing by overriding installation values
  - Updating an application
  - Template functions, variables, conditionals

TP 2 - Creation of a simple Helm Chart:
  - Recuperating a chart to examine it’s structure
  - Creation of a new Chart
  - Customized Chart installation using the ‘--set’  option
  - Customized Chart installation using the ‘-f values.yaml’  option
  - Use of the ‘dry-run’ option

Advanced Helm:
  - Upgrading an application
  - Some useful helm commands
  - Helm Best Practices
  - Use of pre-/post-operation hooks
  - Testing Helm Charts
  - Packaging & dependencies

TP 3 - Upgrades, Rollback:
  - Release management with Helm.
  - Updating an application using new values
  - Rolling back to aTesting Helm Charts
  - Tests des Charts

Questions & Answers, Feedback:
  - Q & A session
  - Course evaluation|




Terraform
