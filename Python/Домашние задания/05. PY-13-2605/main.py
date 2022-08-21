a = int(input('a = '))
b = int(input('b = '))
k = a  # - переменная цикла!
count = 0
while k <= b:
    if k % 3 == 0:
        print(k)
        count += 1
    k += 1

print(f'Количество чисел, кратных 3: {count}')

