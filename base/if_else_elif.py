a = 58
b = 7
if a == b:
    print("a = b")
elif a > b:
    print("a > b")
    if a in range(1, 77):
        print("a is in range from 1 to 76.")
    else:
        print("a is not in range from 1 to 76.")
else:
    print("a < b")
