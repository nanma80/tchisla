#!/usr/bin/env python

import sys
import tchisla as t

if len(sys.argv) == 4:
  filename, target_string, digit_string, digits_count_string = sys.argv

  final_target = int(target_string)
  final_digit = int(digit_string)
  final_digits_count = int(digits_count_string)
elif len(sys.argv) == 3:
  filename, target_string, digit_string = sys.argv

  final_target = int(target_string)
  final_digit = int(digit_string)
  final_digits_count = None

records = t.records.get(final_digit)

if final_target not in records and final_digits_count is None:
  print "No record for {}#{}".format(final_target, final_digit)
else:
  if final_digits_count is None:
    final_digits_count = records[final_target]

  print "{}#{} ({}):".format(final_target, final_digit, final_digits_count)
  t.cheater.solve(final_target, final_digits_count, records)
