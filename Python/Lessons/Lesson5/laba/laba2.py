n = int(input('Введите число: '))

f = 1
for k in range(1, n +1):
    f *= k

print(f'{n}! = {f}')
