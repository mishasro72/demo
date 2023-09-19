def find_it(seq):
    # dect = {}
    # count = 1
    # for i in range(len(seq)):
    #     for y in range(i + 1, len(seq)):
    #         if seq[i] == seq[y]:
    #             count += 1
    #     if seq[i] not in dect:
    #         dect[seq[i]] = count
    #     count = 1
    # for i, i1 in dect.items():
    #     if i1 % 2 != 0:
    #         return(i)
    for i in seq:
        if seq.count(i) % 2 != 0:
            return(i)
        
print(find_it([1, 1, 2, 4, 5, 2, 5])) #TESTING CODE

sew = [1, 3, 4 ,5, 6]
print(*sew)

#print(f"Hello, {input('Enter your name: ')}!")
