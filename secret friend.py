from random import *

n = int(input())
spisok = []
slovar = {}
for _ in range(n):
    spisok.append(input())
while len(slovar) < 3:
    i = choice(spisok)
    y = choice(spisok)
    if i != y and i not in slovar and y not in slovar.values():
        slovar[i] = y
#print(slovar)

for key, value in slovar.items():
    print(key, '-', value)
