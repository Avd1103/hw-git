# Напишите функцию, которая проверяет: является ли слово палиндромом


def world_check(x):
    y = x[::-1]
    if x == y:
        return True
    else:
        return False

x=input('введите слово:')
print(world_check(x))





