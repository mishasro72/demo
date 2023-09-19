def persistence(n):
    count = 0
    while len(str(n)) > 1:
        p = 1 
        spisok = list(str(n))
        for i in spisok:
            p *=int(i) 
        n = p
        count += 1
    return count      

print(persistence(39))
