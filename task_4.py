# Задайте список из элементов, заполненных числами из промежутка [-N, N]. Задайте два числа - позиции(индексы) 
# в исходном списке это границы диапазона. Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16
# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть, что они могут быть некорректными:
# больше длины списка, меньше нуля, первый больше второго и т.п.

import random

def list_number(n):
    list_num = []
    for i in range(-n, n+1):
        list_num.append(random.randint(-n, n))
    return list_num


def sum_interval(str, index_1, index_2):
    sum = 0
    if index_1 > index_2:
        temp = index_1
        index_1 = index_2
        index_2 = temp

    for i in range(index_1, index_2+1):
        sum += str[i]
    return sum


def check_index(n, index_1, index_2):
    result_check = True
    if(index_1 < 0 or index_2 < 0) or (index_1 == index_2) or (index_1 > 2 * n or  index_2 > 2 * n):
        result_check = False
    return result_check


n = int(input("Enter N: "))

index_1 = int(input("Enter start index: "))
index_2 = int(input("Enter end index: "))

if check_index(n, index_1, index_2) == True:    
    str = list_number(n)
    print(str)
    print(sum_interval(str, index_1, index_2))
else: print(f'Проверте введенные индексы {index_1} и {index_2}')