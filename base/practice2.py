def close_fun(n):
    def inner(a):
        nonlocal n
        n += a
        return n

    return inner


f = close_fun(5)
print(f(3))
print(f(3))
print(f(3))
print(f(3))
print()
ff = close_fun(25)
print(ff(5))
print(ff(7))
print(ff(7))
print(ff(7))


def counter():
    n = 0

    def step():
        nonlocal n
        n += 1
        return n

    return step


v = 3
vv = counter()
while v >= -4:
    res = vv()
    print(f"{res} -> {v}.")
    v -= 1
else:
    print("Завершение работы цикла.")
