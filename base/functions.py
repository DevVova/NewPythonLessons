def my_func():
    def inner_func():
        print("Hello!")


    print("Hi!")
    inner_func()

def main():
    my_func()
    print(sum2(3, 4))
    print(sum1(34, 5))


def sum1(a, b):
    return a * b


def sum2(a, b):
    return a + b


main()