def counter():
    n = 0

    def inner():
        nonlocal n
        n += 1
        return n

    return inner


def multiply(a): return lambda b: a * b


def mm(a):

    def kk(n):
        nonlocal a
        a *= n
        return a

    return kk


c = counter()
print(c())
c()
c()
print(c())
res = counter()
print(res(), "\n")

d = multiply(7)
print(d(4))
print(d(77))
print(d(2), "\n")

f = mm(4)
print(f(5))
print(f(5))
print(f(5))