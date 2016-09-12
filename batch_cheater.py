#!/usr/bin/env python

import sys
import requests
import json

filename, check_limit_string = sys.argv
check_limit = int(sys.argv[1])
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
    if digits >=1 and digits <= 9:
      registry[digits][target] = digits_count
  return registry

def check_optimality(target, digits, registry):
  digits_count = registry[target] - 1

  for (operand_1, operand_1_count) in registry.iteritems():
    if operand_1_count >= digits_count:
      continue

    # operand_1 + or - plus_2 == target
    plus_2 = abs(target - operand_1)
    operator = '+' if (target > operand_1) else '-'
    if plus_2 in registry:
      if operand_1_count + registry[plus_2] <= digits_count:
        print "\aFound better solution for {}#{} ({}): {} ({}) {} {} ({})".format(
          target,
          digits,
          digits_count,
          operand_1, operand_1_count,
          operator,
          plus_2, registry[plus_2]
        )
        return

    # operand_1 * times_2 == target
    if target % operand_1 == 0:
      times_2 = target / operand_1
      if times_2 in registry:
        if operand_1_count + registry[times_2] <= digits_count:
          print "\aFound better solution for {}#{} ({}): {} ({}) * {} ({})".format(
            target,
            digits,
            digits_count,
            operand_1, operand_1_count,
            times_2, registry[times_2]
          )
          return

    # numerator / operand_1 == target
    numerator = operand_1 * target
    if numerator <= cache_limit:
      if numerator in registry:
        if operand_1_count + registry[numerator] <= digits_count:
            print "\aFound better solution for {}#{} ({}): {} ({}) / {} ({})".format(
              target, digits, digits_count,
              numerator, registry[numerator],
              operand_1, operand_1_count
            )
            return


records = all_records()
for digits in xrange(1, 10):
  print "Processing #{}".format(digits)

  for target in xrange(1, check_limit + 1):
    sub_records = records[digits]
    if target not in sub_records:
      print "No record for {}#{}".format(target, digits)
    else:
      check_optimality(target, digits, sub_records)
