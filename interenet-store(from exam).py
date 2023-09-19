n = int(input())
spisok = {}
for i in range(n):
    a, b, c = input().split()
    spisok[a] = spisok.get(a, {})
    spisok[a][b] = spisok.get(a, {}).get(b, 0) + int(c)
for i in sorted(spisok):
    print(f'{i}:', sep='\n')
    for k in sorted(spisok[i]):
        print(f'{k} {spisok[i][k]}', sep='\n')
