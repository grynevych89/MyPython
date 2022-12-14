# Создаем список:
s1 = {'Мария Ивановна', 'Аркадий Абрамович', 'Игорь Васильевич', 'Роза Остаповна',
      'Октябрина Аркадиевна', 'Абрам Абрамович', 'Валентина Ивановна', 'Иван Олегович',
      'Евгений Валерьевич', 'Владимир Владимирович', 'Клавдия Марковна'
      }
print(f'Льготники №1: {s1}')
s2 = {
    'Мария Ивановна', 'Абрам Абрамович', 'Клавдия Марковна', 'Иван Олегович',
    'Октябрина Аркадиевна', 'Арсений Григорьевич', 'Марк Олегович',
    'Наталия Александровна', 'Александо Владимирович', 'Инна Александровна'
}
print(f'Льготники №2: {s2}')

# Выводим список тех, кто получает только одну из льгот:
d1 = s1.difference(s2)
d2 = s2.difference(s1)
print(f'Список тех, кто получает только льготу №1: {d1}')
print(f'Список тех, кто получает только льготу №2: {d2}')

# Выводим список тех, кто получает обе льготы:
print(f'Список тех, кто получает обе льготы: {s1.intersection(s2)}')
