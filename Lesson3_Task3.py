import unittest
from Lesson3_4 import ITEmployee

class EmployeeWithoutPositionTest(unittest.TestCase):

    """Precondition"""
    def setUp(self):
        self.emp = ITEmployee("Elena", "Pian")

    # """Tests"""

    def test_names(self):
        self.assertEqual(self.emp.name, "Elena")
        self.assertEqual(self.emp.surname, "Pian")

    def test_no_position(self):
        self.assertIsNone(self.emp.position)

    def test_no_skills(self):
        self.assertEqual(len(self.emp.skills), 0)

    def test_add_position(self):
        self.emp.set_position('QA Engineer')
        self.assertEqual(self.emp.position, 'QA Engineer')

    def test_add_one_skill(self):
        self.emp.add_skills('git')
        self.assertIn('git', self.emp.skills)

if __name__ == "__main__":
    unittest.main()