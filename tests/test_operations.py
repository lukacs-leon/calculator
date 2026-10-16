import unittest

from calculator.operations import Operations


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operations = Operations()

    def test_add(self):
        self.assertEqual(self.operations.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.operations.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.operations.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.operations.divide(12, 3), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.operations.divide(5, 0)


if __name__ == "__main__":
    unittest.main()