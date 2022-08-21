name = input('Как Вас зовут? - ')
print(f'Будем знакомы, {name}!')

age = int(input('Сколько Вам лет? - '))
benefit = 65 - age
print(f'{name}, а до пенсии Вам осталось: {benefit} лет')

radius = float(input('Введите радиус окружности: '))
s = round(3.14 * radius ** 2, 2)
print(f'Площадь круга: s = {s}')
