from random import randint

a = [randint(10, 99) for k in range(5)]
print(a)

n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            buff = a[j]
            a[j] = a[j + 1]
            a[j + 1] = buff

print(a)
