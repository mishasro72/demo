from random import uniform as uni

n = 10**6       # количество испытаний
k = 0

for _ in range(n):
    x = uni(-2, 2)
    y = uni(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
        k += 1
print((k/n) * 16)


