# list_1 = ['a', 'b', 1, 5, 6, 'hello']
# sum = 0
# for i in list_1:
#     if  type(i) is int:
#         sum += i
# print(sum)

# pets = ['cat', 'dog', 'bird']
# print(set(pets))

# family_1 = list([x for x in input().split(',')])
# family_2 = list([x for x in input().split(',')])

# if len(family_1) > len(family_2):
#     print (family_1)
# elif family_2 > family_1:
#     print(family_2)
# else:
#     print('Equal')

# my_dict = {'num' : 357, 'num_1' : 340, 'num_2': 500, 'srt' : 'bob'}
# sum = 0
# for i in my_dict.values():
#     if type(i) is int:
#         sum += i
# print(sum)


# spisok = [1, 3, 4, 5, 5, 4, 3, 8]

# print(set(spisok))

my_set_1 = {1, 4, 5, 'd', 'f', 'g'}
my_set_2 = {1, 4, 5, 'd', 'f', 'g', 'k', 9}

print(my_set_1.intersection(my_set_2))
print(my_set_2.difference(my_set_1))
print(my_set_1.issubset(my_set_2))
print(my_set_2.issubset(my_set_1))



