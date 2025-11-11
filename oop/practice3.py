class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I'm {self.name}.")

    def do(self):
        print(f"Human {self.name} is doing.")


class Employee:
    def __init__(self, any_name):
        self.name = any_name

    def do(self):
        print(f"Employee {self.name} is doing.")

class Men(Human, Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def hi(self):
        print(f"Hi! I'm {self.name}. I'm {self.age} years old.")


ted = Men("Ted", 44)
ted.hi()