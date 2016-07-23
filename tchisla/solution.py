class Solution():
  """Solution for number # base"""
  registry = {}
  known_improvements = {
    # 2: {
    #   3: [64]
    # }
    6: {
      2: [216]
    }
  }

  def __init__(self, number, base, complexity, operator=None, input_1=None, input_2=None):
    self.number = number
    self.base = base
    self.input_1 = input_1
    self.input_2 = input_2
    self.operator = operator
    self.complexity = complexity

  def formatted(self):
    formula = ''

    if self.input_1 is None:
      formula = ''
    elif self.input_2 is None:
      if self.operator == '!':
        formula = '{} {}'.format(self.input_1.number, self.operator)
      else:
        formula = '{} {}'.format(self.operator, self.input_1.number)
    else:
      formula = '{} {} {}'.format(self.input_1.number, self.operator, self.input_2.number)

    return '{}: {}, {}'.format(self.number, self.complexity, formula)

  @classmethod
  def register(cls, solution):
    # only register the first time because the complexity is minimum
    if solution.number not in cls.registry:
      cls.registry[solution.number] = solution
