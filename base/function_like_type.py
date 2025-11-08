def print_hello(): print("Hello.")


def sum1(a, b): return a + b


def multiply(a, b): return a * b


# Функция как параметр функции
def do_operation(a, b, op):
    return op(a, b)


# Функция как результат функции
def select_operation(choice):
    if choice == 1:
        return sum1
    else:
        return multiply



pr = print_hello
pr()
operation = sum1
print(operation(23, 34))
operation = multiply
print(operation(22, 4))
print(do_operation(44, 67, sum1))
print(do_operation(35, 56, operation))
ch = select_operation(3)
print(ch(45, 2))