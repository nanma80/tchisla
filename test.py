import sympy
import tchisla as t

collection = t.Collection(6)
collection.build(5)
for solution in collection.iter_solution():
  print sympy.Rational(357)/solution.number
