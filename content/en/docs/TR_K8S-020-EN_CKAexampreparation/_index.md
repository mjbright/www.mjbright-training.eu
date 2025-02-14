---
title: K8S-020-EN CKA exam preparation
weight: 1020
---
**Duration: 1 day**

The objective of this single day training is to prepare to take the Linux Foundation “CKA - Certified Kubernetes Administrator” exam.

Participants will be challenged with various exam-like tasks to perform - see below for more details.

The training consists of about 90% hands-on labs.


# Training Outcomes

The training participant will be well prepared to take the certification


# Target Audience

This training is ideal for engineers who already have some experience with Kubernetes administration.
**Note:** Following K8S-002-EN & K8S-004-EN trainings alone is not sufficient to succeed in certification - much practice is necessary.   This training will provide tips, practical exercises and resources to help prepare for the exam.

# Pre-requisites

To take full advantage of this training, participants:
- should be at ease working at the command line
- have basic notions of Linux processes
- have basic notions of container engines such as Docker
- Be able to use an SSH client such as openssh on Linux, macOS, WSL or Putty on Windows

If lacking command-line skills it is advised to first follow the training “LIN-001-EN - Introduction a Linux - en ligne de commande / shell” or equivalent.
Participants must provide their own PC with internet access, with the ability:
- to use a browser to connect to sites hosted on AWS
- to connect to AWS EC2 VMs using SSH: alternative connection methods can be provided

Participants should already have a first experience with the theory and practice of administering Kubernetes - having followed the “K8S-002-EN Administration Kubernetes” training for example or équivalent.


# Evaluation

At the beginning of the training we will verify the domain experience, if any, and any expectations of each participant.


# Programme

During the day, participants will be challenged with practical tasks to accomplish similar to those encountered in the exam, for example:
- Implement a scénario
  - a Deployment where the Pods access a ConfigMap mounted as a Volume
  - a DaemonSet where the Pods access a Secret via environment variables
  - prevent Pods in the ‘frontend’ Namespace ‘frontend’ being able to communicate with Pods in the ‘backend’ Namespace
- Debug scenarios
  - a Service which fails to respond to requests, or is intermittent
  - a Pod which fails to start, or a Container which continually restarts
  - kubectl timing out|


