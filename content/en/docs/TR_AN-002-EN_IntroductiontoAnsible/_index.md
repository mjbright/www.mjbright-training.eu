---
title: AN-002-EN Introduction to Ansible
weight: 802
---
**Duration: 2 days**

This training proposed as a 2-day training, or 5 half-days, provides a comprehensive introduction to Configuration Management using Ansible.


**Note:** This training also exists as a 3-day training “AN-003-EN Introduction to Ansible” allowing more time for labs and also the addition of “Ansible Vault” and “Network Automation” modules.


This training includes much hands-on as well as theory.
All hands-on exercises will be performed on Linux Virtual Machines & Containers.


Students will appreciate the ease with which software can be installed & maintained in a reliable, repeatable and reusable manner across teams thanks to the largely declarative nature of Ansible Playbooks & Roles.   Playbooks can be re-run guaranteeing repeatable outcomes due to the idempotent nature of Ansible..|

# Pre-requisites

Be at ease working at the command-line, editing files
Basic notions of Cloud, Linux, Containers
Use of an ssh Client, e.g. openssh on Linux, macOS or Windows (or Putty)
|

# Included

Course materials and labs: 50% hands-on, 50% presentation & demos
Access to a temporary lab environment
Access to an evolutive document covering various learning resources
|

# Objectives

Learn to use Ansible for performing software configuration & maintenance of machines/devices
Learn about the many builtin modules, collections of modules & roles for Ansible
Learn best practices for working with Ansible
|


# Programme



**Module: Introduction**

- Why Ansible?
- Concepts & Terms
- Agentless Architecture
- Inventory
  - Static & Dynamic
  - Host & Group Patterns


**Module: Deploying with Ansible**

- Installing Ansible
- YAML Configuration Files
- Playbooks
  - Ansible Modules
  - Ad-Hoc Commands
  - Dynamic Inventory
    - Scripted
    - Plugins


**Exercise**

- Deploying Ansible
- Ad-Hoc Commands
- Dynamic Inventories


**Module: Playbooks**

- Playbook structure
- Host and Task Execution Order
- Module Categories
  - Command
  - File Manipulation
  - Network Modules
  - Packaging Modules
  - System Storage
  - Account Management
  - Security
  - Services


**Exercise**

- Playbook Basics
- Playbooks: Command Modules
- Playbooks: Common Modules


**Module: Variables**

- at runtime
- in Playbooks
- register task output, debug module
- in inventory: host_vars, global_vars
- Scope & precedence
- Facts & magic variables
- In included files, roles
- Output: callback plugins


**Exercise**

- Variables and Facts
- Inclusions


**Module: Jinja Templating**

- Jinja Expressions
- Builtin.template module
- Filters
- Methods
- Conditionals
- Lookup plugins
- Control Structures


**Exercise**

- Jinja Templates


**Module: Control Structures**

- Loops & Variables (with)
- Conditionals (when)
- Handlers
- Tags
- Error Handling


**Exercise**

- Task Control


**Module: Roles**

- Usage
- Creating Roles
- Deploying Roles with Ansible Galaxy


**Exercise**

- Converting Playbooks to Roles
- Creating Roles from Scratch
- Ansible Galaxy Roles


**Exercise**

- Optimizing Ansible|

