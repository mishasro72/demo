from re import *

def solution(s):
    # l = 0
    # spisok = []
    # for i in range(2, len(s) + 1, 2):
    #     spisok.append(s[l:i])
    #     l += 2
    # if len(s) % 2 != 0:
    #     spisok.append(s[-1] + '_')
    # return(spisok)
    return findall('...', s + '_')

print(solution('abcdef'))


