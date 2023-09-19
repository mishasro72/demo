# spoken    = lambda greeting: greeting + '.'
# shouted   = lambda greeting: greeting.upper() + '!'
# whispered = lambda greeting: greeting.lower() + '.'

# greet = lambda style, msg:  style(msg)

# print(greet(spoken, 'Hello'))

from functools import reduce


current_list = [5, 15, 20]
summa = reduce((lambda x, y: x + y), current_list)
razn = reduce((lambda x, y: x - y), current_list)
delen = reduce((lambda x, y: x / y), current_list)
print(summa, razn, delen)
