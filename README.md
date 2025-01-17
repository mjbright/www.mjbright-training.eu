# @mjbright Consulting / Hugo / Docsy Module Notes

# Installation

## Install Postcss

```
npm install postcss
```

## Source of this site

## Modifying top menu items

e.g. for 
content/en/blog/_index.md

modify Title in frontmatter

## Creating top menu items

Create content/en/trainings/_index.md with front matter:

```
---
title: Trainings
menu: {main: {weight: 30}}
---
```
Create content/fr/trainings/_index.md with front matter:

```
---
title: Formations
menu: {main: {weight: 30}}
---
```

## Creating a new annual newsletter

```
mkdir                    content/en/blog/news/2025-newsletter/
hugo new content -k post content/en/blog/news/2025-newsletter/index.md
```

