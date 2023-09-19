# def converter (a):
#     color = ''
#     list1 = list(filter(lambda x: x != 'x', list(hex(a))))
#     list1 = list1[1:]
#     for i in list1:
#         if i.isalpha():
#             color += i.upper()
#         else:
#             color += i
#     if len(color) < 2:
#         color = '0' + color
#     return color

# def rgb(r, g, b):
#     arguments = locals()
#     for k, i in arguments.items():
#         if i < 0:
#             arguments[k] = 0
#         elif i > 255:
#             arguments[k] = 255
#     print(arguments)
#     return converter(arguments['r']) + converter(arguments['g']) + converter(arguments['b']) 
    
# print(rgb(0, 0, 0))  # Выводит: 0xf5

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
print(rgb(255, 0, 0))
