from records import *

def check_optimality(target, digits_count, registry, cache_limit = DEFAULT_CACHE_LIMIT):
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