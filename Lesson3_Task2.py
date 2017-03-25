import unittest
from Lesson2_Task3 import distance
from Lesson2_Task4 import is_year_leap
from Lesson2_Task5 import check_triangle_existence

class DistanceTests(unittest.TestCase):

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


class YearTests(unittest.TestCase):

    """Precondition"""
    def setUp(self):
        pass

    # """Tests"""
    def test_leap_multiple_of_4(self):
        self.assertTrue(is_year_leap(2016))

    def test_leap_multiple_of_400(self):
        self.assertTrue(is_year_leap(2000))

    def test_leap_multiple_of_100(self):
        self.assertFalse(is_year_leap(1900))

    def test_notleap(self):
        self.assertFalse(is_year_leap(2017))


class TriangleTests(unittest.TestCase):

    """Precondition"""
    def setUp(self):
        pass

    # """Tests"""
    def test_zero(self):
        self.assertFalse(check_triangle_existence(0, 0, 0))

    def test_one(self):
        self.assertTrue(check_triangle_existence(1, 1, 1))

    def test_two(self):
        self.assertTrue(check_triangle_existence(2, 2, 2))

    def test_three(self):
        self.assertFalse(check_triangle_existence(0, 1, 2))

    def test_three(self):
        self.assertFalse(check_triangle_existence(3, 1, 2))

if __name__ == "__main__":
    unittest.main()