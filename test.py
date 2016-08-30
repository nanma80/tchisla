import sympy
import tchisla as t

target_pairs = [(804, 6), (867, 7)]

collection = t.Collection(8)
collection.build(6)
print len(t.Solution.registry)

for (target, target_digits) in target_pairs:
  for solution1 in collection.iter_solution():
    value1 = solution1.number
    if value1 < 0:
      continue
    value2 = sympy.Rational(1) * target / value1
    if value2 in t.Solution.registry:
      solution2 = t.Solution.registry[value2]
      if solution1.complexity + solution2.complexity <= target_digits:
        print "Found solution for ", target
        print solution1.formatted()
        print solution2.formatted()
        break
