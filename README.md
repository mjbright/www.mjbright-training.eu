# @mjbright Consulting / Hugo / Docsy Module Notes

# Installation

## Install Postcss

```
npm install postcss
```

## Weird things seen

- top-level language selection no longer working ...
- page not displaying (but page right-hand ToC OK, print view OK)
  - fixed by renaming _index.md as index.md (why??)

## Source of this site

## Modifying top menu items

e.g. for 
content/en/blog/_index.md

modify Title in frontmatter

## Modify colors

Edit file assets/scss/_variables_project.scss, e.g. adding

For RGB:
```
/* Modifying colors:
  $primary: #f90040;
  $secondary: #000072;
  $success: #004b00;
*/
```

**Note:** will be pastelized when used with ```{{% pageinfo color="primary" %}} color=primary {{% /pageinfo %}}```

## Add colors

assets/scss/_variables_project_after_bs.scss. For example:

$custom-colors: (
  'my-favorite-color': purple,
  'my-other-color': pink,
);

$theme-colors: map-merge($theme-colors, $custom-colors);


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

