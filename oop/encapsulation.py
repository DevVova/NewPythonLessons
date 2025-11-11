class House:
    def __init__(self, house_price):
        self.__price = house_price
        self.__country = "USA"
        self.color = "White"

    def set_country(self, country):
        self.__country = country

    def get_country(self):
        return self.__country

    def info(self):
        print(f"Price - {self.__price}. Color - {self.color}. Country - {self.__country}.")


my_house = House(34000)
my_house.info()
# Изменить приватный атрибут можно только способом ниже.
my_house._House__price = 45000
my_house.info()
print(my_house.get_country())
my_house.set_country("Russia")
my_house.info()
print("-----------------------------------------\n")


class Person:
    def __init__(self, age, name):
        self.__name = name
        self.__age = age

# Ниже нужно соблюдать такой именно порядок, сначала геттер, потом сеттер.
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, number):
        if 0 > number > 140:
            print("Возраст не соответствует действительности.")
            self.__age = 1
        else:
            self.__age = number

    def info(self):
        print(f"Hello! I'm {self.__name}. I am {self.__age} years old.")


vova = Person(47, "Vova")
vova.info()
vova.age = 48
vova.info()