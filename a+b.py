# n = int(input())
def fill_out(n):
    matrix = []
    for _ in range(n + 1):
        matrix.append([1] + [0] * n)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            matrix[i][j] = matrix[i -1][j] + matrix[i - 1][j - 1]
    return matrix

def formula(n):
    matrix = fill_out(n)
    # for i in matrix:
    #     print(i)
    string = "a^" + str(n)
    k = 1
    for i in range(1, n + 1):
        string += '+'
        string += str(matrix[n][k]) + 'a^' + str(n - k) + 'b'
        k += 1
    string = string.replace('1','')
    string = string.replace('0', '')
    print(string)
# print(fill_out(5))
# fill_out(5)
formula(2)
