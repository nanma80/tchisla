# import math
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
      fraction_part_output = sympy.N(output % 1)

      if fraction_part_output < 0.01 or fraction_part_output > 0.99:
        return None

      return output
      # if output % 1 == 0:
      #   return int(output)
      # else:
      #   return None

    def factorial(input):
      input_n = sympy.N(input)
      if input_n < 30 and input_n > 0 and input_n % 1 == 0:
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
      return input_1 + input_2

    def subtract(input_1, input_2):
      result = input_1 - input_2
      result_n = sympy.N(result)
      if result_n > 0:
        return result
      else:
        return None

    def times(input_1, input_2):
      return input_1 * input_2

    def divide(input_1, input_2):
      # print input_1, input_2
      if input_2 == 0:
        return None
      result = sympy.Rational(1) * input_1 / input_2
      result_n = sympy.N(result)
      if result_n < 1 and result_n > 1.0 - 0.1**5:
        return None
      if result_n > 1 and result_n < 1.0 + 0.1**5:
        return None
      return result

    def power(input_1, input_2):
      input_2_n = sympy.N(input_2)

      if input_2_n > 30 or input_2_n < -30:
        return None

      fraction_part_input_2 = sympy.N(input_2 % 1)

      if (input_2 % 1 != 0) and (fraction_part_input_2 < 0.1 ** 6 or fraction_part_input_2 > 1 - 0.1 ** 6):
        return None

      if sympy.N(input_1) <= 0:
        return None
      result = input_1 ** input_2
      result_n = sympy.N(result)
      if result_n < 10 ** 30 and result_n > 0.1 ** 30:
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
