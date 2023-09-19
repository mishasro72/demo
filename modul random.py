from random import *

#for _ in range(10):
 #   print(random.randint(1,10))

#print(random.random())

#random.seed(17)

#for _ in range(10):
 #   print(random.randint(1, 100))


#from random import * # модель броска костей

#n = int(input())    # количество попыток

#for _ in range(n):
 #   print(randint(1,6))


#from random import * # модель броска монеты

#n = int(input())

#for _ in range(n):
 # if randint(1, 2) == 1:
  #  print("Орел")
  #else:
   # print("Решка")

#from random import * # моделирование генерации пароля заданной длины

#length = int(input())
#passw =  ""

#for _ in range(length):
 #   if randint(1, 2) == 1:
  #      passw += chr(randint(65, 90))
   # else:
    #    passw += chr(randint(97, 122))
#print(passw)

#from random import * # модель случайных чисел лотереи

#lottery = []
#for _ in range(7):
 #   a = randint(1, 49)
  #  while a in lottery:
   #     a = randint(1, 49)
    #lottery.append(a)
#print(*sorted(lottery), sep = " ")

#from random import * # модель случайных чисел лотереи решение через множество

#lottery = set()
#while len(lottery) < 7: 
 #   lottery.add(randint(1, 49))
#print(*sorted(lottery), sep = " ")

#num = [x for x in range(15)]
#print(num)
#shuffle(num)
#print(num)

#from string import *
#srt = ascii_letters
#print(srt)

#def generate_ip(): # функция генереации валидного ip решение № 1
 #   ip = []
    #return('.'.join([str(x) for x in randrange(256) for _ in range(4)]))
  #  for _ in range(4):
   #     ip.append(str(randrange(256)))
    #return('.'.join(ip))
 #   return('.'.join(str(choice(range(256))) for _ in range(4)))
#print(generate_ip())
from string import ascii_uppercase as letter
def generate_index(): #LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 
   # letter = ascii_uppercase
    index = []
    for _ in range(2):
        index.append(choice(letter))
    index.append(str(randrange(100)))
    index.append("_")
    index.append(str(randrange(100)))
    for _ in range(2):
        index.append(choice(letter))
    return "".join(index)
print(generate_index())

