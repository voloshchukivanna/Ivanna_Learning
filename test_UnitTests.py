import unittest
from triangle import hyp


class TestHyp(unittest.TestCase):
    def test_zero_triangle(self):
        r = hyp(0, 0)
        self.assertEqual(r, 0)

    def test_3_4_triangle(self):
        r = hyp(3, 4)
        self.assertEqual(r, 5)

if __name__== "__main__":
    unittest.main()