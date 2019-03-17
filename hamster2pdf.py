#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import hamster.client
import reports
import argparse
import pdfkit
import gettext
gettext.install('brainz', '../datas/translations/')

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

htmlFilename = os.path.splitext(args.reportFile)[0]+".html"
pdfFilename = os.path.splitext(args.reportFile)[0]+".pdf"

storage = hamster.client.Storage()
facts = storage.get_todays_facts()

# generate report

reports.simple(facts, args.startDate, args.endDate, htmlFilename)

# convert .html to .pdf file:

pdfkit.from_file(htmlFilename, pdfFilename)
