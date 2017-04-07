import unittest
from Lesson3_Task1 import Employee

class EmployeeTests(unittest.TestCase):

    """Precondition"""

    def setUp(self):
        self.emp = Employee('Chumak Julia Volodymyrivna', 'QA', 1500, 3)

    # """Tests"""

    def test_names(self):
        self.assertEqual(self.emp.name, 'Chumak Julia Volodymyrivna')
        self.assertEqual(self.emp.position, 'QA')
        self.assertEqual(self.emp.salary, 1500)
        self.assertEqual(self.emp.experience, 3)