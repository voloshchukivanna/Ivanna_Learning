class Person:
    common = [3, 56]

    def __init__(self, name = "", surname = "", age = 0):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return self.name + " " + self.surname

    def get_older(self, year):
        self.age += year


if __name__== "__main__":
    o = Person("Ivanna", "Voloshchuk", 32)
    print(o.age)

    o.get_older(5)
    print(o.age)

    # o1 = Person("Tom", "Black", 35)

    # print(o.full_name())
    # print(o.name)
    # print(o1.age)
    # o.name = "Ivanna"
    # print(o.name)
    # print(o1.name)
    # print(o.common)
    # print(o1.common)


    # class Employee:
    #     pass