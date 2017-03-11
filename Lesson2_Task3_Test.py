import unittest
from Lesson2_Task3 import distance

class PositiveTest(unittest.TestCase):

    """Precondition"""
    def setUp(self):
        pass

    # """Tests"""
    def test_zero(self):
        res = distance(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_one(self):
        res = distance(0, 0, 0, 1)
        self.assertEqual(res, 1)

    def test_two(self):
        res = distance(0, 0, 1, 1)
        self.assertEqual(res, 2 ** 0.5)

    def test_three(self):
        res = distance(0, 1, 1, 0)
        self.assertEqual(res, 2 ** 0.5)



if __name__ == "__main__":
    unittest.main()