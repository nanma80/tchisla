import math
from records import *

reverse_factorial = {}
for n in xrange(3, 20):
  reverse_factorial[math.factorial(n)] = n


def solve(target, digits_count, registry, cache_limit=DEFAULT_CACHE_LIMIT, suppress_failure=False):
  if target > 1:
    # sqrt(square) == target
    square = target ** 2
    if square in registry and registry[square] <= digits_count:
      print "{} ({}) = sqrt({})".format(
        target,
        digits_count,
        square
      )
      return solve(square, registry[square], registry)

  # rev_fac! == target
  if target in reverse_factorial:
    rev_fac = reverse_factorial[target]
    if rev_fac in registry and registry[rev_fac] <= digits_count:
      print "{} ({}) = {}!".format(
        target,
        digits_count,
        rev_fac
      )
      return solve(rev_fac, registry[rev_fac], registry)

  for (operand_1, operand_1_count) in registry.iteritems():
    if operand_1 == 'digits':
      continue

    if operand_1_count >= digits_count:
      continue

    # operand_1 ** power == target
    if operand_1 > 1:
      power = int(math.log(target, operand_1) + 0.5)

      if operand_1 ** power == target:
        if power in registry and operand_1_count + registry[power] <= digits_count:
          print "{} ({}) = {} ^ {}".format(
            target,
            digits_count,
            operand_1,
            power,
          )
          operand_1_solved = solve(operand_1, operand_1_count, registry)
          other_solved = solve(power, registry[power], registry)
          return operand_1_solved and other_solved

    # operand_1 + or - plus_2 == target
    plus_2 = abs(target - operand_1)
    operator = '+' if (target > operand_1) else '-'
    if plus_2 in registry:
      if operand_1_count + registry[plus_2] <= digits_count:
        print "{} ({}) = {} {} {}".format(
          target,
          digits_count,
          operand_1,
          operator,
          plus_2
        )
        operand_1_solved = solve(operand_1, operand_1_count, registry)
        other_solved = solve(plus_2, registry[plus_2], registry)
        return operand_1_solved and other_solved

    # operand_1 * times_2 == target
    if target % operand_1 == 0:
      times_2 = target / operand_1
      if times_2 in registry:
        if operand_1_count + registry[times_2] <= digits_count:
          print "{} ({}) = {} * {}".format(
            target,
            digits_count,
            operand_1,
            times_2
          )
          operand_1_solved = solve(operand_1, operand_1_count, registry)
          other_solved = solve(times_2, registry[times_2], registry)
          return operand_1_solved and other_solved

    # numerator / operand_1 == target
    numerator = operand_1 * target
    if numerator <= cache_limit:
      if numerator in registry:
        if operand_1_count + registry[numerator] <= digits_count:
            print "{} ({}) = {} / {}".format(
              target, digits_count,
              numerator,
              operand_1,
            )
            other_solved = solve(numerator, registry[numerator], registry)
            operand_1_solved = solve(operand_1, operand_1_count, registry)
            return other_solved and operand_1_solved

  if str(target) == str(registry['digits']) * digits_count:
    return True

  if not suppress_failure:
    print "{} ({}) = ?".format(target, digits_count)
  return False
