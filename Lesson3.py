# def word_printer(word, count=1, wow=0):
#     if wow == 1:
#         print((word * count).upper())
#     else:
#         print(word * count)
#
#
# word_printer(3, "Bob")

# print(dir(dict()))


class Employee:
    title = "Infopulse Employee"
    def __init__(self, name, surname, position=None):
        self.name = name
        self.surname = surname
        self.position = position

    def set_name(self, name):
        self.name = name
    def set_surname(self, surname):
        self.surname = surname
    def set_position(self, position):
        self.position = position

    def full_name(self):
        return self.name + " " + self.surname

    def find_position(self):
        if self.position is None:
            return " is not employed"
        else:
            return " works as " + self.position

if __name__ == "__main__":
    print("TEST TEST")

a = Employee("Julia", "Ivanova")
# print(a.full_name() + a.find_position())

b = Employee("Oleg", "Petrov", "QA")
# print(b.full_name() + b.find_position())

