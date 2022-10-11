# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def list_number(n):
    list_num = []
    m = 1
    for i in range(n):
        m = round(((1 + 1 / (i + 1)) ** (i+1)), 2)
        list_num.append(m)
    return list_num


def sum_number(str):
    sum = 0
    for i in range(len(str)):
            sum += str[i]
        
    return sum


n = int(input("Enter N: "))
str = list_number(n)

print(f'Для n = {n}: {str}')
print(f'Cумма {sum_number(str)}')