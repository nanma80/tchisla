import sympy
import tchisla as t

target = 1898
target_digits = 7

collection = t.Collection(2)
collection.build(5)
print len(t.Solution.registry)

for solution1 in collection.iter_solution():
  if solution1.complexity > 4:
    continue
  if sympy.N(solution1.number) < 0.1 ** 10 or sympy.N(solution1.number) > 10.0 ** 10:
    continue
  print solution1.number
  for solution2 in collection.iter_solution():
    if (
      sympy.N(solution2.number) < target * 1.1 / sympy.N(solution1.number) and
      solution1.complexity + solution2.complexity <= target_digits and
      solution1.number * solution2.number == target
    ):
      print "Found solution"
      print solution1.formatted()
      print solution2.formatted()
