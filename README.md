UPDATE by vleg1991:

Here, I've integrated the forked script with HTML report generation engine by Hamster.


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

It will output both .html and .pdf files.


## Sample output (.pdf file)

See [sample.pdf](sample.pdf)

## Dependecies

Uses `pdfkit`

```
pip install pdfkit
```