#!/usr/bin/env python

import sys
import tchisla as t

filename, target_lower_bound_string, target_upper_bound_string, digit_string = sys.argv

target_lower_bound = int(target_lower_bound_string)
target_upper_bound = int(target_upper_bound_string)
final_digit = int(digit_string)

records = t.records.get(final_digit)
print "#{}".format(final_digit)
for final_target in xrange(target_lower_bound, target_upper_bound + 1):
  final_digits_count = records[final_target]
  print "{}#{} ({})".format(final_target, final_digit, final_digits_count)
  t.cheater.solve(final_target, final_digits_count, records)
  print
