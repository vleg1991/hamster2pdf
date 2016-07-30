#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import hamster.client
import argparse
import pypandoc

# custom settings:

reportTitle = "My Activities Report"
activityFilter = "unfiled"

def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

# find dates:

today = datetime.date.today()
first = today.replace(day=1)
previousLast = first - datetime.timedelta(days=1)
previousFirst = previousLast.replace(day=1)

# assign arguments:

parser = argparse.ArgumentParser(description="export the hamster database to pdf")
parser.add_argument("--thismonth", action="store_true", help="export this month's records")
parser.add_argument("--lastmonth", action="store_true", help="export last month's records")
parser.add_argument("-s", dest="startDate", default=today, help="start date (default: today)", type=valid_date)
parser.add_argument("-e", dest="endDate", default=today, help="end date (default: today)", type=valid_date)
parser.add_argument("-o", dest="reportFile", default="report.pdf", help="output file (default: report.pdf)")

# parse arguments:

args = parser.parse_args()

if args.thismonth:
	args.startDate = first
	args.endDate = today

if args.lastmonth:
	args.startDate = previousFirst
	args.endDate = previousLast

# prepare filenames:

mdFilename = os.path.splitext(args.reportFile)[0]+".md"
pdfFilename = os.path.splitext(args.reportFile)[0]+".pdf"

# write out header block:

mdFile = open(mdFilename, "w")

mdFile.write("---\n")
mdFile.write("title: '**%s %s - %s**'\n" % (reportTitle, args.startDate, args.endDate))
mdFile.write("...\n\n")

# read hamster database and export hamster records to .md file:

storage = hamster.client.Storage()
recordCount = 0

for fact in storage.get_facts(args.startDate, args.endDate):
	if fact.activity == activityFilter:
		continue
	recordCount +=1
	tags = "#"+", #".join(fact.tags)
	tags = ("" if tags == "#" else tags)
	mdFile.write("**%s** %s@%s\n" % (fact.date, fact.activity, fact.category))
	mdFile.write("---\n")
	mdFile.write("`%s`\n\n%s\n\n" % (tags, fact.description))

mdFile.close()

# convert .md to .pdf file:

pdoc_args = ["-V", "geometry: margin=2.5cm", "-V", "papersize: a4paper"]
pdfFile = pypandoc.convert(mdFilename, "pdf", outputfile=pdfFilename, extra_args=pdoc_args)

# results:

print recordCount, "records from", args.startDate, "to", args.endDate, "exported to", pdfFilename
