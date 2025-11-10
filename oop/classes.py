class Person:
    def __init__(self, name, age):
        self.person_name = name # атрибут объекта
        self.person_age = age
        print("Объект создан.")

    def say_hello(self):
        print(f"Hello {self.person_name}")

    def __del__(self):
        print(f"Объект с именем {self.person_name} удалён.")


def creat_person():
    sam = Person("Sam", 54)
    print(sam.person_name)


class Animal:
    name = "Ted" # атрибут класса
    color = "Grey"
    def __init__(self):
        print("Created an animal.")

    # Если не передавать self, то только так. Это статический метод для всего класса.
    # Не имеет доступа к атрибутам класса или объекта.
    @staticmethod
    def info():
        print("Dog")

    @classmethod
    def wow(cls):
        print(f"Wow!!! {cls.color}")


vova = Person(age=47, name="Vova")
vova.say_hello()

creat_person()

bob = Animal()
ted = Animal.name
print(Animal.name)
Animal.info()
bob.info()
Animal.wow()
bob.wow()
