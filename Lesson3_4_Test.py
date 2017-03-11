import unittest
from Lesson3_4 import ITEmployee

class EmpNoPositionTests(unittest.TestCase):

    def test_creation(self):
        exp = ITEmployee("Elena", "Pian")
        self.assertEqual(exp.name, "Elena")
        self.assertEqual(exp.surname, "Pian")

        self.assertEqual(exp.position, None)
        self.assertIsNone(exp.position)

        self.assertEqual(len(exp.skills), 0)

        n = ITEmployee("Oleg", "Petrenko")
        n.add_skills("Python")
        n.add_skills("Quality Assurance")
        n.add_skills("Project Management")

        self.assertEqual(n.name, "Oleg")

class NegativeTests(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()