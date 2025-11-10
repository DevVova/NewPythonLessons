def decor(fun):
    def inner(*args):
        my_list = list(args)
        for i in range(len(my_list)):
            my_list[i] *= 5
        fun(*my_list)

    return inner


@decor
def my_multiply(*args):
    for i in args:
        print(i, end=" ")
    print()


def decor2(fun):
    def inner(*args):
        l = []
        for i in args:
            l.append(i * 10)
        return fun(*l)

    return inner


@decor2
def sum5(*args):
    res = 0
    for i in args:
        res += i

    return res


my_multiply(5, 9, 34, 4)
print(sum5(2, 4, 5))

tuple1 = (23, 12, 44, 35)
list1 = [i * 5 for i in tuple1]
for i in list1:
    print(i, end=" ")
print()

tuple2 = (3, 22, 2, 87)
list2 = []
for i in tuple2:
    list2.append(i * 10)
    print(i * 10, end=" ")
print("\n")
for i in list2:
    print(i, end="  ")