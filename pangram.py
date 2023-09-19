def is_pangram(s):
    alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
    s = s.lower()
    for i in s:
        if i in alphabet:
            alphabet.remove(i)
    if alphabet:
        return False
    else:
        return True
    
print(is_pangram('The quick brown fox jumps over the lazy dog'))
