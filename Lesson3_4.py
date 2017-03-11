from Lesson3 import Employee

class ITEmployee(Employee):
    def __init__(self, name=None, surname=None, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self.skills = []

    def add_skills(self, new_skill):
        self.skills.append(new_skill)


n = ITEmployee("Oleg", "Petrenko")
n.add_skills("Python")
n.add_skills("Quality Assurance")
n.add_skills("Project Management")

#
# print(n.full_name(), " is experienced at ", n.skills)
