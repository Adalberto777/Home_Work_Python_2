# Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно
import random


def mix_str(str):
    str_index = [] # создаем строку для перемешивания индексов
    str_mix = [] # создаем массив для итоговых результатов
    get_index = 0 # переменная 
    for i in range(len(str)):
        while str_index.count(get_index) != 0:
            get_index = random.randint(0, len(str)-1)
        str_index.append(get_index)

    for i in str_index:
        str_mix.append(str[i])

    return str_mix 
      

str = ['p', 'r' , 'i', 'v', 'e', 't', 6, 7, 8, 9]

print(str)
print(mix_str(str))