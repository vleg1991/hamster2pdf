UPDATE by vleg1991:

Here, I've integrated the forked script with HTML report generation engine by Hamster.

```

## New Dependecies

Uses `pdfkit`

```


# hamster2pdf.py

Reads the activities, contexts, tags and descriptions from the [Hamster Time Tracker](https://github.com/projecthamster/hamster)
database and outputs them sorted by date to MarkDown and PDF files. Does not
output task start and end times or durations.

Look at the sample output below.

## Usage

```
./hamster2pdf.py [-h] [--thismonth] [--lastmonth] [-s STARTDATE] [-e ENDDATE] [-o REPORTFILE]
```

 * `--thismonth` - export this month's records
 * `--lastmonth` - export last month's records
 * `-s <start date>` - start date (default: today)
 * `-e <end date>` - end date (default: today)
 * `-o <filename>` - output file (default: report.pdf)

The dates must be given in `YYYY-MM-DD` format.

It will output both .md and .pdf files.

## Sample output (.md file)

```
---
title: '**My Activities Report 2016-06-01 - 2016-06-30**'
...

**2016-06-04** documentation@project1
---
`#documentation`

Writing online documentation for Project 1.

**2016-06-04** maintenance@customer2
---
`#maintenance`

Rebuild RAID array at database server. Swapped out one dead drive.

**2016-06-05** development@office
---
`#development`

Added new features to application. More unit tests.
```

## Sample output (.pdf file)

See [sample.pdf](sample.pdf)

## Custom settings

The following settings can be changed in the `hamster2pdf.py` file:

 * `reportTitle` - report title
 * `activityFilter` - do NOT include activities containing the given string

## Dependecies

Uses `pandoc` and `pdflatex` for `.md -> .pdf` conversion. Also a wrapper
for `pandoc` - [pypandoc](https://github.com/bebraw/pypandoc).

On Fedora 23:

```
dnf install pandoc
dnf install python2-pypandoc
dnf install texlive
```
