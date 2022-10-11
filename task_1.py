# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44
def sum_num(str):
    sum = 0
    str_mod = (str.translate({ord(i): None for i in ',.-+'}))
    for i in range(len(str_mod)):
        sum += int(str_mod[i])
    return sum


print('Enter N')
str = input()

print(sum_num(str))