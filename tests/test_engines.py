import unittest

from calculator.engines.native import NativeEngine


class TestNativeEngine(unittest.TestCase):

    def setUp(self):
        self.engine = NativeEngine()

    def test_add(self):
        self.assertEqual(self.engine.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.engine.subtract(9, 4), 5)

    def test_multiply(self):
        self.assertEqual(self.engine.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.engine.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.engine.divide(10, 0)


if __name__ == "__main__":
    unittest.main()