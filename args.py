def sum(*аrgs): # использование *args позволяет передать лбое количество 
                 #  аргументво в функцию sum (можно использрвать лобое слово вместо args) 
    res = 0
    for i in аrgs:
        res += i
    return res

print(sum(1, 2, 3, 4, 5))

def diction(**kwars):
    return kwars

print(diction(a = 'Apple', b = 'Banan'))
