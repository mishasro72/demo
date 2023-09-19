def order(sentence):
    text_1 = []
    text = list([x for x in sentence.split()])
    for i in range(1, len(text) + 1):
        for slovo in text:
            if str(i) in slovo:
                text_1.append(slovo)
    sentence = ''
    for i in text_1:
         sentence += i + " "
    sentence = sentence.rstrip()
    return sentence

print(order(""))
