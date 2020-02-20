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

api_records = t.records.get_api_records()

unsolved_count = 0
unknown_count = 0

for digits in xrange(final_digit_lower_bound, final_digit_upper_bound + 1):
  print "Processing #{}".format(digits)

  for target in xrange(target_lower_bound, target_upper_bound + 1):
    if target % 1000 == 0:
      print target
    remote_records = api_records[digits]

    result = t.cheater.solve(target, remote_records[target] - 1, remote_records, fail_fast=True, suppress_failure=True)
    if result != None:
      print result

