import unittest

from pymath.constant import pi, e


class ConstantTest(unittest.TestCase):

    def test_pi(self):
        self.assertAlmostEqual(pi, 3.1415, places=3)

    def test_e(self):
        self.assertAlmostEqual(e, 2.7182, places=3)
