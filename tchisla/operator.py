import sympy

class Operator(object):
  unary = ['sqrt', '!', '-']
  binary = ['+', '-', '*', '/', '^']

  @classmethod
  def apply_unary(cls, operator, input_1):
    def sqrt(input):
      if sympy.N(input) <= 0:
        return None
      output = sympy.sqrt(input)
      if output.is_rational:
        return output
      else:
        return None

    def factorial(input):
      if sympy.N(input) < 30 and sympy.N(input) > 0 and input.is_integer:
        return sympy.factorial(input)
      else:
        return None

    def negate(input):
      return (-input)

    return {
      'sqrt': sqrt,
      '!': factorial,
      '-': negate
    }[operator](input_1)

  @classmethod
  def apply_binary(cls, operator, input_1, input_2):
    def add(input_1, input_2):
      if sympy.N(input_2) <= 0:
        return None
      return input_1 + input_2

    def subtract(input_1, input_2):
      if sympy.N(input_2) <= 0:
        return None
      result = input_1 - input_2
      if sympy.N(result) > 0:
        return result
      else:
        return None

    def times(input_1, input_2):
      if sympy.N(input_2) <= 0:
        return None
      result = input_1 * input_2
      result_n = sympy.N(result)
      if result_n < 10 ** 41 and result_n > 0.1 ** 16:
        return result
      else:
        return None

    def divide(input_1, input_2):
      if input_2 <= 0:
        return None
      result = sympy.Rational(1) * input_1 / input_2
      result_n = sympy.N(result)
      if result.is_rational and result_n < 10 ** 41 and result_n > 0.1 ** 16:
        return result
      else:
        return None

    def power(input_1, input_2):
      if sympy.N(input_1) <= 0:
        return None
      input_2_n = sympy.N(input_2)
      if input_2_n > 30 or input_2_n < -30:
        return None
      if not input_2.is_integer:
        return None

      result = input_1 ** input_2
      result_n = sympy.N(result)

      if result_n < 10 ** 41 and result_n > 0.1 ** 16:
        return result
      else:
        return None

    return {
      '+': add,
      '-': subtract,
      '*': times,
      '/': divide,
      '^': power
    }[operator](input_1, input_2)
