import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(5, 2)
        self.assertEqual(result, 2.5)

    def test_divide_by_zero(self):
        calc = Calculator()

        with self.assertRaises(ValueError):
            calc.divide(5, 0)

    # ---- Q6: modulo ----
    def test_modulo(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(7, 3), 1)    # 7 = 2*3 + 1
        self.assertEqual(calc.modulo(10, 5), 0)   # divisible -> 0
        self.assertEqual(calc.modulo(2, 5), 2)    # a < b -> a

        
if __name__ == "__main__":
    unittest.main()