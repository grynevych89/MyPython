from sities import *

if __name__ == '__main__':
    words = create_dict()
    eng = input('Введите название страны: ')
    a = words
    sity_name = capital(words, eng)
    print(sity_name)
