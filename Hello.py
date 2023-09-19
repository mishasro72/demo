#name, surname = input(), input()

#print("Name:", name, "Surname:", surname)

# num = int(input())
# print(num // 10000)

# from math import *

# l = [1, 2, 3, 4]
# print(prod(l))

# i = int(input())
# assert i != 0, "был введен 0"

# from datetime import *

# print (date.today().year)

# def squre(x): # вернуть кортеж из элекинтов: периметр квадрата, площадь и длина диагонали
#    return tuple(i for i in (4 * x, x * x, round(((x ** 2 + x ** 2) ** 0.5), 2)))

# print(squre(2))

# from functools import * #  найти впроизведение всех элементов списка
# my_list = [1 ,2, 3, 4, -7, -9, 10]
# pow = reduce(lambda x, y: x * y, my_list)  
# print(pow)

# def s_count(s, x): # найти количество вхождений запрашиваего элемента в строку
#     return s.count(x)

# print(s_count('aa_bb_cc_bb_bb_cc', 'bb'))


def count_vowes(s): # найти сколько гластных в строке
    vowes = 'aeiou'
    return len(list(filter(lambda x: x in vowes, s)))

print(count_vowes('ggaaaryuu'))




