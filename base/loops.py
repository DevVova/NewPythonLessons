i = 0
res = 0
while i < 7:
    print(i, end=" ")
    res += i
    i += 1
else: print()
print(res, end="\n")

for n in range(4, 19, 5):
    print(n, end=" ")
print("\n")

max_num = 22
for nn in range(4, max_num + 1):
    if nn < max_num:
        print(nn, end=", ")
    else:
        print(nn, end=".")
else:
    print("\nThe End!")

for a in range(1, 10):
    for b in range(1, 10):
        print(f"{a * b}", end="\t")
    print()

print()
for x in range(10):
    if x == 3:
        continue
    if x == 8:
        break
    print(x, end=" ")    