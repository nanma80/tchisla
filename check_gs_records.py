#!/usr/bin/env python

import sys
import tchisla as t

if len(sys.argv) == 2:
  filename, target_lower_bound_string = sys.argv
  target_upper_bound_string = target_lower_bound_string
  digit_lower_bound_string = '1'
  digit_upper_bound_string = '9'
elif len(sys.argv) == 3:
  filename, target_lower_bound_string, target_upper_bound_string = sys.argv
  digit_lower_bound_string = '1'
  digit_upper_bound_string = '9'
elif len(sys.argv) == 4:
  filename, target_lower_bound_string, target_upper_bound_string, digit_lower_bound_string = sys.argv
  digit_upper_bound_string = digit_lower_bound_string
elif len(sys.argv) == 5:
  filename, target_lower_bound_string, target_upper_bound_string, digit_lower_bound_string, digit_upper_bound_string = sys.argv

target_lower_bound = int(target_lower_bound_string)
target_upper_bound = int(target_upper_bound_string)
final_digit_lower_bound = int(digit_lower_bound_string)
final_digit_upper_bound = int(digit_upper_bound_string)


gs_records = t.records.get_gs_records()
api_records = t.records.get_all(merge_gs_records=False)

for digits in xrange(final_digit_lower_bound, final_digit_upper_bound + 1):
  print "#{}:".format(digits)

  for target in xrange(target_lower_bound, target_upper_bound + 1):
    api_sub_records = api_records[digits]
    gs_sub_records = gs_records[digits]

    if target not in gs_sub_records:
      print "No GS record for {}#{}".format(target, digits)
    elif target not in api_sub_records:
      # API records are known to be incomplete
      pass
    else:
      if api_sub_records[target] != gs_sub_records[target]:
        print "{}#{}: API: {}; GS: {}".format(target, digits, api_sub_records[target], gs_sub_records[target])
  print
