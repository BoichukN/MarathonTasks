# Write the function quadratic_equation with arguments a, b ,c
# that solution to quadratic equation without comlex solution.
# Write unit tests for this function with QuadraticEquationTest class

import unittest


def quadratic_equation(a, b, c):
    if a != 0:
        d = b * b - 4 * a * c
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if d > 0:
            return x1, x2
        elif d == 0:
            return x1
        elif d < 0:
            return None
    else:
        raise ValueError


class QuadraticEquationTest(unittest.TestCase):

    def test_divide_zero(self):
        self.assertEqual(quadratic_equation(2, 4, 2), -1.0)

    def test_positive(self):
        self.assertEqual(quadratic_equation(2, -30, 0), (15.0, 0.0))

    def test_negative(self):
        self.assertEqual(quadratic_equation(1, 0, 36), None)

    def test_error(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)
