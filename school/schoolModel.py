from school.group import Group, Student, Teacher
from school.personal import Personal


class School:
    def __init__(self, name, groups: list, personals: list):
        self.__name = name
        self.__groups = groups
        self.__personals = personals
        self.__teachers = []

    def __str__(self):
        return f'{self.__name}'

    def add_group(self, new_group):
        if type(new_group) == Group:
            self.__groups.append(new_group)
            return True
        return False

    def add_personal(self, new_personal):
        if type(new_personal) == Personal:
            self.__groups.append(new_personal)
            return True
        return False

    def remove_group(self, number):
        for group in self.__groups:
            if group.number == number:
                self.__groups.remove(group)
                return True
        return False

    def remove_personal(self, name, last_name):
        for personal in self.__personals:
            if personal.name == name and personal.last_name == last_name:
                self.__personals.remove(personal)
                return True
        return False

    def formation_teachers(self ):
        for group in self.__groups:
            self.__teachers.extend(group.teachers)
        self.__teachers = list(set(self.__teachers))
        return self.__teachers

s1 = Student("Ivan", "Petrov", 19, 4)
s2 = Student("Petr", "Petrov", 19, 4)
t1 = Teacher("Alex", "Sidorov", 76, 34)
t2 = Teacher("Semen", "Sidorov", 34, 4)
t3 = Teacher("Qwert", "Sidorov", 34, 4)
g1 = Group(1, [s1, s2], [t1, t2])
g2 = Group(2, [s1, s2], [t2, t1, t3])
s = School("name", [g1, g2], [])

ts = s.formation_teachers()
for i in s.formation_teachers():
    print(i)





