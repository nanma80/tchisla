from solution import *
from operator import *


class Generation():
  generations = {}

  def __init__(self, index, base):
    self.index = index
    self.base = base
    self.solutions = set()

  def build(self):
    single_number = (10 ** self.index - 1) / 9 * self.base
    first_solution = Solution(single_number, self.base, self.index)

    seeds = [first_solution]
    if self.base in Solution.known_improvements:
      if self.index in Solution.known_improvements[self.base]:
        numbers = Solution.known_improvements[self.base][self.index]
        for number in numbers:
          seeds.append(Solution(number, self.base, self.index))

    for input_1_index in xrange(1, self.index):
      input_2_index = self.index - input_1_index
      for input_1 in Generation.generations[input_1_index].solutions:
        for input_2 in Generation.generations[input_2_index].solutions:
          for operator in Operator.binary:
            result = Operator.apply_binary(operator, input_1.number, input_2.number)
            if (result is not None) and (result not in Solution.registry):
              new_solution = Solution(result, self.base, input_1.complexity + input_2.complexity, operator, input_1, input_2)
              seeds.append(new_solution)
              Solution.register(new_solution)

    for seed in seeds:
      Solution.register(seed)

      for operator in Operator.unary:
        result = Operator.apply_unary(operator, seed.number)
        if (result is not None) and (result not in Solution.registry):
          new_solution = Solution(result, self.base, seed.complexity, operator, seed)
          seeds.append(new_solution)
          Solution.register(new_solution)

    self.solutions = set(seeds)
    Generation.generations[self.index] = self
