def visikosnii(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('Високосный')
    else:
        print('Невисокосный')


year = int(input('Введите год: '))
visikosnii(year)


