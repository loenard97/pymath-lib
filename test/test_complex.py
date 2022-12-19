import unittest

from pymath.complex import Complex


class ComplexTest(unittest.TestCase):

    def test_abs(self):
        self.assertEqual(abs(Complex(0, 1)), 1)

    def test_add(self):
        self.assertEqual(Complex(1, 2) + Complex(2, 3), Complex(3, 5))

    def test_sub(self):
        self.assertEqual(Complex(1, 2) - Complex(2, 3), Complex(-1, -1))

    def test_mul(self):
        self.assertEqual(Complex(1, 2) * Complex(2, 3), Complex(-4, 7))

    # def test_div(self):
    #     self.assertEqual(Complex(1, 2) / Complex(2, 3), Complex(3, 5))
