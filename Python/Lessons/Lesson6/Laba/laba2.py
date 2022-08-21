usd_sale = 27.5
usd_buy = 28.11
euro_sale = 33.6
euro_buy = 33.8

while True:

    print('==============================')
    print(' Простейший Конвертер валют')
    print('==============================')
    print('    1 - Купить доллары')
    print('    2 - Продать доллары')
    print('    3 - Купить Евро')
    print('    4 - Продать Евро')
    print('    5 - Выйти из программы')
    print('==============================')

    try:
        operation = int(input('Выберите номер нужного действия: '))
        if operation == 1:
            amount = float(input('Введите желаемую сумму для покупки: '))
            result = amount * usd_sale
            print(f'Вам потребуется - {result} uah')
        elif operation == 2:
            amount = float(input('Введите желаемую сумму для продажи: '))
            result = amount / usd_buy
            print(f'Ваши {amount} uah - К выдаче: {result} usd')
        elif operation == 3:
            amount = float(input('Введите желаемую сумму для покупки: '))
            result = amount * euro_sale
            print(f'Вам потребуется - {result} uah')
        elif operation == 4:
            amount = float(input('Введите желаемую сумму для продажи: '))
            result = amount / euro_buy
            print(f'Ваши {amount} uah - К выдаче: {result} euro')
        elif operation == 5:
            break
        else:
            raise RuntimeError('Вы выбрали несуществующий вариант')
    except ValueError as err1:
        print(f'Ошибка ввода => {err1}')
    except RuntimeError as err2:
        print(err2)

        choice = input('Продолжать (y/n)? - ')
        if choice == 'n':
            break
        else:
            pass
