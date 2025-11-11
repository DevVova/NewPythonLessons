class Person:
    def __init__(self, name):
        self.__name = name
        self.age = 33

    def __del__(self):
        print("The person deleted.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def info(self):
        print(f"I'm {self.__name}.")

class Men:
    def __init__(self, name):
        self.__name = name

    def do(self):
        print(f"The men {self.__name} is doing.")

class Employee(Person):
    def work(self):
        print(f"{self.name} is working. He is {self.age} years old.")

    def do(self):
        print(f"Employee {self.name} is doing.")


class Student(Employee, Men):
    def __init__(self, name):
        super().__init__(name)

    def study(self):
        print(f"Student {self.name} is studying.")


kolya = Employee("Kolya")
kolya.name = "Kolyan"
print(kolya.name)
kolya.info()
kolya.work()
print("---------------------------")
gena = Student("Gena")
gena.do()