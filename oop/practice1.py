class Human:
    name = "Human"

    def __init__(self, human_age):
        self.age = human_age
        print("Human created!")

    def __del__(self):
        print(f"Human with {self.age} deleted!")

    def info(self):
        print(f"Hi! I'm {self.name}. I am {self.age} years old.")

    @classmethod
    def info_name(cls):
        print(f"I'm {cls.name}")
        print("@@@@@@@@@@@@@@@@@@@")
        cls.info(Human(33))

    @staticmethod
    def info_country():
        print("I'm from USA.")

vova = Human(47)
print("------------------------")
vova.info()
print("++++++++++++++++++++++++")
vova.name = "Vova"
print(">>>>>>>>>>>>>>>>>>>>>>>>>")
vova.info()
print("++++++++++++++++++++++++")
Human.info_name()
print("oooooooooooooooooooooooooooo")
vova.info_name()
print("++++++++++++++++++++++++")
Human.info_country()