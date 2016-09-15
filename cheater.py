#!/usr/bin/env python

import sys
import requests
import json

filename, target_string, digit_string, digits_count_string = sys.argv

final_target = int(target_string)
final_digit = int(digit_string)
final_digits_count = int(digits_count_string)

cache_limit = 1000000000

def all_records():
  registry = {}
  for digits in xrange(1, 10):
    registry[digits] = {}
  resp = requests.get("http://www.euclidea.xyz/api/v1/game/numbers/solutions/records?&query={gte:1,lte:" + repr(cache_limit) + "}")
  all_records = json.loads(resp.content)['records']
  print "loaded {0} records from API".format(len(all_records))

  for record in all_records:
    digits = int(record['digits'])
    target = int(record['target'])
    digits_count = int(record['digits_count'])
    if digits == final_digit:
      registry[target] = digits_count
  return registry

def check_optimality(target, digits_count, registry):
  for (operand_1, operand_1_count) in registry.iteritems():
    if operand_1_count >= digits_count:
      continue

    # operand_1 + or - plus_2 == target
    plus_2 = abs(target - operand_1)
    operator = '+' if (target > operand_1) else '-'
    if plus_2 in registry:
      if operand_1_count + registry[plus_2] <= digits_count:
        print "{} ({}) = {} ({}) {} {} ({})".format(
          target,
          digits_count,
          operand_1, operand_1_count,
          operator,
          plus_2, registry[plus_2]
        )
        check_optimality(operand_1, operand_1_count, registry)
        check_optimality(plus_2, registry[plus_2], registry)
        return

    # operand_1 * times_2 == target
    if target % operand_1 == 0:
      times_2 = target / operand_1
      if times_2 in registry:
        if operand_1_count + registry[times_2] <= digits_count:
          print "{} ({}) = {} ({}) * {} ({})".format(
            target,
            digits_count,
            operand_1, operand_1_count,
            times_2, registry[times_2]
          )
          check_optimality(operand_1, operand_1_count, registry)
          check_optimality(times_2, registry[times_2], registry)

          return

    # numerator / operand_1 == target
    numerator = operand_1 * target
    if numerator <= cache_limit:
      if numerator in registry:
        if operand_1_count + registry[numerator] <= digits_count:
            print "{} ({}) = {} ({}) / {} ({})".format(
              target, digits_count,
              numerator, registry[numerator],
              operand_1, operand_1_count
            )
            check_optimality(numerator, registry[numerator], registry)
            check_optimality(operand_1, operand_1_count, registry)
            return

records = all_records()
print "#{}".format(final_digit)
check_optimality(final_target, final_digits_count, records)
