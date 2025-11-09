def decor(any_func):
    def outer():
        print("This is decorator.")
        any_func()

    return outer


def new_sum(sum1):
    def outer(*args):
        print("This is a new sum.")
        return sum1(*args)

    return outer


def not_zero(outer):
    def inner(*args):
        res = outer(*args)
        if res < 0: res = 0
        return res

    return inner


@decor
def hi():
    print("Hi!")


@new_sum
def sum2(a, b):
    return a + b


@not_zero
def sum3(a, b):
    return a + b


hi()
print(sum2(56, 22))
print(sum3(29, -10))
