# Лямбда-выражения в языке Python представляют
# небольшие анонимные функции, которые определяются с помощью оператора lambda.
def do_operation(a, b, op):
    print(f"Result = {op(a, b)}")


def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


sum1 = lambda a, b: a + b
print(sum1(67, 45))
do_operation(55, 55, lambda a, b: a * b)
s = select_operation(4)
print(s(22, 2))
