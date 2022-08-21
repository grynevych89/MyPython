from models.cats import Cats
from models.dogs import Dogs
from models.bird import Bird
from models.fish import Fish


if __name__ == '__main__':
    cat = Cats(
        name='Кошка',
        type_animal='Млекопитающее',
        kingdom='Животные',
        type_a='Хордовые',
        infra_class='Плацетарные',
        detachment='Хищные',
        family='Кошачьи',
        genus='Кошки',
        view='Лесная Кошка',
        subspecies='Домашняя кошка',
        lat_name='Felis silvestris catus'
    )
    print(cat)

    dog = Dogs(
        name='Собака',
        type_animal='Млекопитающее',
        kingdom='Животные',
        type_a='Хордовые',
        detachment='Хищные',
        family='Псовые',
        genus='Волки',
        view='Волк',
        subspecies='Собака',
        del_type='Ездовые, Охотничьи, Пастушьи',
        lat_name='Canis lupus familiaris'
    )
    print(dog)

    bird = Bird(
        name='Птица',
        type_animal='Птицы',
        kingdom='Животные',
        type_a='Хордовые',
        detachment='',
        family='',
        genus='Птицы',
        view='Птица',
        subspecies='Бескилевые, Новонебные',
        sniper='Точное попадание в цель какашками'
    )
    print(bird)

    fish = Fish(
        name='Рыба',
        type_animal='Рыбы',
        kingdom='Животные',
        type_a='Хордовые',
        detachment='',
        family='',
        genus='Рыбы',
        view='Рыба',
        subspecies='',
        ultimate='Быстро плавает, но очень вкусная'
    )
    print(fish)
