def func1(age, name="Vova"):
    print(f"Name is {name}. Age is {age}.")


# Все параметры, которые располагаются справа от символа *, получают значения только по имени:
def fun(country, *, age, name="Vova"):
    print(f"I'm {name}. I am from {country}. I'm {age} years old.")


# Если наоборот надо определить параметры, которым можно передавать
# значения только по позиции, то есть позиционные параметры, то можно
# использовать символ /: все параметры, которые идут до символа / ,
# являются позиционными и могут получать значения только по позиции
def fun2(age, name="Sasha", /):
    print(f"I'm {name}. I'm {age} years old.")


# Неопределенное количество параметров
def fun_more(*numbers):
    res = 0
    for x in numbers:
        res += x
    print(res)


func1(33)
func1(29, "Fill")
func1(name="Andrey", age=12)
fun("USA", age=25)
fun2(24)
fun_more(23, 2, 34, 44, 44444, 5, 5)