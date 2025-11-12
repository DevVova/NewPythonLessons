def decor_for_human(fun):
    def outer(*args):
        print("Hello!")
        fun(*args)

    return outer


class Human:
    def __init__(self, name, age):
        self.name_h = name
        self.age_h = age

    def info(self):
        print(f"This is a human. He is {self.name_h}.")

class Person(Human):
    def __init__(self, name, age, county):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.country = county

    def __del__(self):
        print(f"Person {self.__name} deleted.")

    @property
    def age(self): return self.__age

    @age.setter
    def age(self, age_input):
        if 0 > age_input > 130:
            self.__age = 1
            print("Возраст был не верно введён.")
        else: self.__age = age_input

    @decor_for_human
    def info_with_outer_name(self, name):
        print(f"I'm {name}.")

    def info(self):
        super().info()
        print("This is a person.")


vova = Person("Vova", 47, "Kazakhstan.")
print(vova.age)
vova.info_with_outer_name("Helen")
vova.info()
print(isinstance(vova, Person))
print(isinstance(vova, Human))