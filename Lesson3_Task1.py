class Employee:
    title = "Employee"

    def __init__(self, name, position, salary, experience):
        self.name = name
        self.position = position
        self.salary = salary
        self.experience = experience

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def set_salary(self,salary):
        self.salary = salary

    def set_experience(self, experience):
        self.experience = experience

    def get_surname(self):
        surname = self.name.split()[0]
        return surname

    def get_name(self):
        name = self.name.split()[1]
        return name

    def calculate_salary(self, months):
        total_salary = self.salary * months
        return total_salary

    def get_position_level(self):
        if self.experience < 3:
            return "Junior " + self.position
        elif self.experience >= 3 and self.experience <= 6:
            return "Middle " + self.position
        else:
            return "Senior " + self.position


employee_1 = Employee("Chumak Julia Vladimirovna", "QA", 1500, 3)

print (employee_1.get_surname())
print (employee_1.get_name())
print(employee_1.calculate_salary(3))
print(employee_1.get_position_level())