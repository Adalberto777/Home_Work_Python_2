# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def list_number(n):
    list_num = []
    m = 1

    for i in range(n):
        m *= (i + 1)
        list_num.append(m)
        
    return list_num


n = int(input("Enter N: "))
print(list_number(n))