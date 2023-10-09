def __init__(self, name):
    self.name = name
    self.pet = None 

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass
class Salmon(Fish):
    pass
class Halibut(Fish):
    pass

rover = Dog("")