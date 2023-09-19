# def duplicate_count(text):
#     text1 = list(text.lower())
#     n = 0
#     for i in text1:
#         if text1.count(i) > 1:
#             n += 1
#             text1 = list(filter(lambda x: x != i, text1))
#     return n

def duplicate_count(text):
    # text = (text.lower())
    # text1 = set()
    # #n = 0
    # for i in text:
    #     if text.count(i) > 1:
    #         text1.add(i)
    #        # n += 1
    #         #text1 = list(filter(lambda x: x != i, text1))
    # return len(text1)

    #return (len([x for x in set(text.lower()) if text.lower().count(x) > 1]))

    return len((set(filter(lambda x: text.lower().count(x) > 1, text.lower()))))


print(duplicate_count('n98XMoinmc9n2fAF7h6awoiXI1'))
