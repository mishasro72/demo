def sum_inter(a, b):
    # if a < b:
    #     return(sum([x for x in range(a, b + 1)]))
    # else:
    #     return(sum([x for x in range(b, a + 1)]))
    return(sum(range(min(a, b), max (a,b))))

print (sum_inter(0, -1))

str = ""

# if str is True:
#     print('yes')
# else:
#     print("no")
# print(bool({}))
