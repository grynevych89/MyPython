from lingvo import *

if __name__ == '__main__':
    words = create_dict()
    #
    eng = input('Введите слово для перевода: ')
    trans = translate(words, eng)
    print(trans)
    print(words)

