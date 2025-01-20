#!/usr/bin/env /Users/mjb/scripts/HASHBANG_PYTHON3_venv.sh rtf

# !/usr/bin/env python3

from striprtf.striprtf import rtf_to_text

import sys
# For die context:
from inspect import currentframe, getframeinfo

#import re
import os

# -- Func: -------------------------------------------------------------------

def die(msg):
    previous_frame_info = getframeinfo(currentframe().f_back)
    context = [previous_frame_info.filename, str(previous_frame_info.lineno)]
    sys.stderr.write(f'die: line {context[1]}@{context[0]}:\n  {msg}\n')
    sys.exit(1)


def readfile(path, mode='r'):
    ifd = open(path, mode)

    # line1=ifd.readline()
    # for line in ifd.readlines(): print(line)
    ret = ifd.read()
    ifd.close()

    return ret


def writefile(path, text='hello world\n', mode='w'):
    ofd = open(path, mode)
    ofd.write(text)
    ofd.close()


def pr_line(prefix, line=''):
    global CURRENT_TRAINING_TEXT, CURRENT_TRAINING_TITLE

    if prefix == '':
        print(line)
        if CURRENT_TRAINING_TITLE != '':
            CURRENT_TRAINING_TEXT += line + '\n'
        return
    print(prefix + line)
    if CURRENT_TRAINING_TITLE != '':
        CURRENT_TRAINING_TEXT += line + '\n'
    return

# -- Args: -------------------------------------------------------------------

SIMPLE_LISTS = False
VERBOSE = False
a = 1
#CATALOG_FILE = 'Catalog_English.rtf'
CATALOG_FILE = 'Catalog.rtf'

while a < len(sys.argv):
    if sys.argv[a] == '-v':
        VERBOSE = True
        print("VERBOSE mode on")
        a += 1
        continue

    CATALOG_FILE = sys.argv[a]
    a += 1

# -- Main: -------------------------------------------------------------------

ENGLISH = True
cwd = os.getcwd()
if  '/en' in cwd:
    ENGLISH = True
if  '/fr' in cwd:
    ENGLISH = False
#if 'english' in CATALOG_FILE.lower():
#if 'french' in CATALOG_FILE.lower():

if ENGLISH:
    print("Running in ENGLISH mode")
else:
    print("Running in FRENCH mode")

with open(CATALOG_FILE) as infile:
    content = infile.read()
    lines = rtf_to_text(content).split('\n')

writefile('/tmp/catalog.rtf.txt', '\n'.join(lines))

LIST_LEVEL = 0
n = 0
IN_TRAININGS_SECTION=False
IN_ADAPTATION_SECTION=False
#title: Trainings
#linkTitle: Trainings
TRAINING_INDEX_TEXT_EN='''
---
title: Training Catalog
menu: {main: {weight: 10}}
---

{{% pageinfo %}}
__PAGE_INFO__
{{% /pageinfo %}}

<a class="btn btn-lg btn-secondary me-3 mb-4" href="cv.pdf">
  [English] Catalog Download <i class="fa-regular fa-newspaper"></i>
</a>

'''

IGNORE='''
It has several categories:
- Containers
  - Kubernetes
  - Docker
- Infrastructure as Code
  - Terraform
  - Ansible [*Configuration Management*]
- Policy Management
  - Kyverno
  - OPA/Rego [*Open Policy Agent*]
'''

CURRENT_TRAINING_TITLE=''
CURRENT_TRAINING_TEXT=''
CURRENT_TRAINING_DIR=''
CURRENT_TRAINING_FILE=''
NEW_TRAINING=False

course_dirs = []
course_keys = []
course_titles = []

# START DOCUMENT:
for line in lines:
    n += 1
    P = ''
    if VERBOSE: P = str(n)+': '
    if VERBOSE: pr_line(P, f'INITIAL {line}')
    #print(type(line))
    #print(dir(line))

    # START ADAPTATION SECTION:
    if not IN_ADAPTATION_SECTION and line == 'Adaptation':
        IN_ADAPTATION_SECTION=True
        a_line = 0
        CURRENT_TRAINING_TITLE = 'ADAPTATION'
        pr_line(P, '### Adaptation')
        continue

    if IN_ADAPTATION_SECTION:
        a_line += 1

        if line == 'Legend' or line == 'Legende':
            IN_ADAPTATION_SECTION=False
            #PAGE_INFO = ''
            PAGE_INFO = CURRENT_TRAINING_TEXT
            #PAGE_INFO = 'CURRENT_TRAINING_TEXT'
   
            TRAINING_INDEX_TEXT_EN = TRAINING_INDEX_TEXT_EN.replace('__PAGE_INFO__', PAGE_INFO)
            CURRENT_TRAINING_TITLE = ''
            CURRENT_TRAINING_TEXT = ''
            #line=''
            continue
        #pr_line(P, line)
        if a_line <= 1:
            pr_line(P, line)
            #pr_line(P, f'{a_line}: {line}\n')
        else:
            pr_line(P, f'- {line}')
            #pr_line(P, f'{a_line}: - {line}\n')
        continue

    # START TRAININGS SECTION:
    if line == 'Trainings' or line == 'Formations':
        IN_ADAPTATION_SECTION=False
        IN_TRAININGS_SECTION=True

    if not IN_TRAININGS_SECTION:
        continue

    # DETECT NEW TRAINING:
    if line.startswith('['):
        print(f'LINE={line}')
        print(f'IN_ADAPTATION_SECTION={IN_ADAPTATION_SECTION} IN_TRAININGS_SECTION={ IN_TRAININGS_SECTION}')
        input()
        if CURRENT_TRAINING_TITLE != '':
            # SAVE current training
            if not os.path.exists( CURRENT_TRAINING_DIR):
                os.mkdir(CURRENT_TRAINING_DIR)
            print(f'writefile({CURRENT_TRAINING_FILE})')
            writefile(CURRENT_TRAINING_FILE, text=CURRENT_TRAINING_TEXT)
            
        pos_closeBracket = line.find(']')
        if pos_closeBracket == -1: die("Expected to find ']' in line {line}")
        course_key=line[1+pos_closeBracket:].strip()
        course_duration=line[1:pos_closeBracket]
        if ENGLISH:
            if not course_duration.endswith('d'): die(f"[EN] Bad course duration: {course_duration}")
        else:
            if not course_duration.endswith('j'): die(f"[FR] Bad course duration: {course_duration}")

        course_duration=f'{ course_duration[:-1] }'
        if ENGLISH:
            course_duration+=' day'
        else:
            course_duration+=' jour'
        if course_duration[0] != '1':
            course_duration+='s'

        pos_space = course_key.find(' ')
        if pos_space == -1: die("Expected to find ' ' after course_key in {course_key}")

        course_title = course_key[pos_space:].strip()
        course_key = course_key[:pos_space]
        course_dir=f'TR_{course_key}_{course_title.replace(" ","")}'
        course_keys.append(course_key)
        course_titles.append(course_title)
        course_dirs.append(course_dir)
        CURRENT_TRAINING_TITLE=course_title
        CURRENT_TRAINING_TEXT=''
        CURRENT_TRAINING_DIR=course_dir
        CURRENT_TRAINING_FILE=f'{CURRENT_TRAINING_DIR}/_index.md'
        print(f'course_title={course_title} course_key={course_key} course_duration={course_duration}')
        #die(f'course_title={course_title} course_key={course_key}')
        NEW_TRAINING=True

        # correspondance course_title : not good for regex!
        pos_dash = course_key.find('-')
        course_group = course_key[: pos_dash]
        rest = course_key[pos_dash+1:]

        print(f'course_group={course_group}')
        match course_group :
            case 'K8S' : course_weight = 1000
            case 'TF'  :  course_weight  = 900
            case _     : die(f'Untreated course group {course_group}')

        pos_dash = rest.find('-')
        index = rest[ : pos_dash ]
        course_weight += int(index)

        MATCH_EXAMPLE='''
        if m := re.match(r"(?K8S<mailbox>.+?)@(?P<domain>.+)", "mailbox@example.com"):
             match m.groupdict():
             case {'domain': "gmail.com"}:
                 print(f"A google email address was found")
             case {'domain': domain}:
                 print(f"domain was bound to {repr(domain)}")
        else:
            pass # No match
        '''

        # Front-matter
        pr_line(P, '---')
        pr_line(P, f'title: {course_key} {course_title}')
        pr_line(P, f'weight: {course_weight}')
        pr_line(P, '---')

        pr_line(P, f'# {course_title}')
        pr_line(P, f'**Duration: {course_duration}**\n')
        continue

    # Skip first entry of training
    if NEW_TRAINING:
        LIST_LEVEL = 0
        #if LIST_LEVEL != 0: die(f'Correct list level logic LIST_LEVEL={LIST_LEVEL}'')
        if line != '|':
            NEW_TRAINING=False
        continue

    line = line.rstrip()
    header2s= [
            'Objective', 'Objectives', 'Objectifs',
            'Target Audience', 'Training Outcomes',
            'Pre-requisites', 'Public concerné et pré-requis',
            'Evaluation', 'Programme'
            ]

    if line.startswith("Note:"): line=f'**Note:**{line[5:]}'

    # Careful to keep ':' at end of line:
    # Also inset line-feed before Day (for Day 1):
    if line.startswith("Day ") or line.startswith("Jour "):
        line=f'\n**{line[:-1]}**:'
        LIST_LEVEL = 0 # Hack ?
        #LIST_LEVEL = 1 # Hack ?

    if LIST_LEVEL == 0:
        for header2 in header2s:
            if line == header2:
                pr_line(P, f'\n# {header2}')
                line='' # Hack !
                continue

    if line.endswith(':'):
        if SIMPLE_LISTS:
            LIST_LEVEL = 1
        else:
            LIST_LEVEL += 1
        pr_line(P, line)
        continue

    if LIST_LEVEL > 0:
        if len(line) == 0 or line == '|':
            if SIMPLE_LISTS:
                LIST_LEVEL = 0
            else:
                LIST_LEVEL -= 1
            if VERBOSE: pr_line(P, 'EMPTY')
            pr_line(P)
        else:
            INDENT_LIST = LIST_LEVEL * '  '
            pr_line(P, f'{INDENT_LIST}- {line}')
    else:
        pr_line(P, line)

for course_group in ['K8S', 'TF']:
    match course_group :
        case 'K8S': line='# Kubernetes Trainings'
        case 'TF':  line='# Terraform (/OpenTofu) Trainings'
        case '_':   line='# Other Trainings'

    pr_line('', line)
    TRAINING_INDEX_TEXT_EN += '\n' + line + '\n'

    for c in range(len(course_keys)):
        course_title=course_titles[c]
        course_key=course_keys[c]
        course_dir=course_dirs[c]
        #course_in_a_group=False
        #print(f'{course_group} - {course_key} {course_title}\n')
        if course_group in course_key:
            line=f'- <a href="{course_dir.lower()}/" > {course_key} {course_title} </a>'
            print(line)
            TRAINING_INDEX_TEXT_EN +=  line + '\n'

writefile('_index.md', TRAINING_INDEX_TEXT_EN)

