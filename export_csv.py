#!/usr/bin/env python

import sys
import csv
import tchisla as t

all_records = t.records.load()
records_to_export =[record for record in all_records if int(record['target']) <= 10000]
fieldnames = ['id', 'target', 'digits', 'digits_count', 'creation_date', 'update_date']

print len(records_to_export)

with open('results/tchisla_records.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(fieldnames)
  for record in records_to_export:
    row = [record[fieldname] for fieldname in fieldnames]
    writer.writerow(row)
