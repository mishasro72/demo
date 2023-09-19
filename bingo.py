from random import *
#b = set()
#while len(b) < 25:
 #   b.add(randint(1, 75))
#bingo = list(b)
#x, y = 0, 5
bingo = sample([x for x in range(1, 76)], 25)
bingo[12] = 0
x, y = 0, 5
for _ in range(5):
    for i in bingo[x:y]:
        print(str(i).ljust(3), end = "")
    print()
    x += 5 
    y += 5
    
