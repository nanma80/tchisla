from context import *


class TestStringMethods(unittest.TestCase):
  def test_1(self):
    collection = t.Collection(1)
    collection.build(5)
    registry = t.Solution.registry
    self.assertEqual(registry[4].complexity, 4)
    self.assertEqual(registry[5].complexity, 4)
    self.assertEqual(registry[6].complexity, 3)


if __name__ == '__main__':
  unittest.main()
