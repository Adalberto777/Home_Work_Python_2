# Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно
import random


def mix_str(str):
    str_mod = []
    str_find = 0
    for i in range(len(str)):
        while str_mod.count(str_find) != 0:
            str_find = random.randint(0, len(str)-1)
        str_mod.append(str_find)
    return str_mod  
      

str = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(str)
print(mix_str(str))