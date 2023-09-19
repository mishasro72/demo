#Var 1
# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#     spisok = [] 
#     for i in range(a, b + 1):
#         if i // 10 == 0:
#             spisok.append(i)
#         else:
#             buf = str(i)
#             sum = 0
#             for y in range(0, len(buf)):
#                 sum += int(buf[y]) ** (y + 1)
#             if sum == i:
#                 spisok.append(i)    
#     return spisok

#Var 2
def pow(n):
    return sum(int(x) ** y for y, x in enumerate(str(n), 1))

def sum_dig_pow(a, b):
    return [x for x in range (a, b + 1) if x == pow(x)]

print(sum_dig_pow(89, 100))
#print(1 // 10)
