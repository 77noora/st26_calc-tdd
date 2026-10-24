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

    def test_modulo_negative_operand(self):
        # Decision (student): floor semantics, result takes the sign of the divisor
        calc = Calculator()
        self.assertEqual(calc.modulo(-7, 3), 2)    # -7 = -3*3 + 2
        self.assertEqual(calc.modulo(7, -3), -2)   #  7 = -3*-3 + (-2)
        self.assertEqual(calc.modulo(-7, -3), -1)  # -7 =  2*-3 + (-1)

    def test_modulo_by_zero(self):
        # Decision (student): raise ValueError, consistent with divide
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.modulo(5, 0)
        with self.assertRaises(ValueError):
            calc.modulo(5, 0.0)   # float zero must be rejected too

    # ---- Q6: power ----
    def test_power(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(3, 2), 9)   # catches swapped arguments (b ** a)
        self.assertEqual(calc.power(5, 1), 5)   # exponent 1 -> base

        
if __name__ == "__main__":
    unittest.main()