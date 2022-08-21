a = 75
user_num = 0
count = 0

while True:
    user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
    count += 1
    if user_num == a:
        print(f'Ты угадал число за {count} попыток')
        print('Спасибо за игру')
        break
    elif user_num > a:
        print('Мое число меньше')
    else:
        print('Мое число больше')
