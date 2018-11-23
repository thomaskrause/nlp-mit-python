#!/usr/bin/env python3

import csv

with open('ridges8_gold.csv', 'r') as csvfile:
    exportreader = csv.reader(csvfile, delimiter='\t')
    # first line is header
    next(exportreader)
    for row in exportreader:
        norm = row[5]
        pos = row[6]
        endstr = " "
        if pos == '$.':
            endstr = "\n"
        print(norm + "/" + pos, end=endstr)
        