from Five_Lesson import Person


class Employee(Person):
    def __init__(self, name=None, surname=None, age=None,  salary=0, position=None):
        Person.__init__(self, name, surname, age)
        self.salary = salary
        self.position = position


    def income(self, months=1):
        return self.salary * months



e = Employee("Ivanna", age = 32, salary = 1800)

print(e.name)
print(e.age)
e.get_older(12)
print(e.age)
print(e.income(months=12))


class ITEmployee(Employee):
    pass

ite = ITEmployee
ite.full_name()
