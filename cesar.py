# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cesar = [x for x in input().split(' ')]
# cesar_word = []
# for i in cesar:
#     for a in i:
#         if a.isalpha():
#             if a.isupper():
#                 cesar_word.append(eng_upper_alphabet[(eng_upper_alphabet.find(a) + 13) % 26])
#             elif a.islower():
#                 cesar_word.append(eng_lower_alphabet[(eng_lower_alphabet.find(a) + 13) % 26])
#         else:
#             cesar_word.append(a)
#     cesar_word.append(" ")
# print(* cesar_word[:-1], sep = "")
    
# def rot13(message):
#     eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#     cesar = [x for x in message.split(' ')]
#     cesar_word = []
#     if cesar[-1] == ' ':
#         flag = 1
#     else: 
#         flag = 0
#     for i in cesar:
#         for a in i:
#             if a.isalpha():
#                 if a.isupper():
#                     cesar_word.append(eng_upper_alphabet[(eng_upper_alphabet.find(a) + 13) % 26])
#                 elif a.islower():
#                     cesar_word.append(eng_lower_alphabet[(eng_lower_alphabet.find(a) + 13) % 26])
#             else:
#                 cesar_word.append(a)
#         cesar_word.append(" ")  
#     if flag == 1:
#         return ''. join(str(x) for x in cesar_word).rstrip()
#     else:
#          return ''. join(str(x) for x in cesar_word)

def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

print(rot13('test test '))
