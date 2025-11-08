def print_age(age):
    if age > 130 or age <= 0:
        print(f"Age is not valid.")
        return
    print(f"Age is {age}.")


def double(num):
    return num * 2


print_age(-4)
print(double(77))