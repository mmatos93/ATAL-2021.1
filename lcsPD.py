from random import choice
from time import time

def iniciaMatriz(lista, m, n):
    for i in range(m+1):
        lista.append(list())
        for j in range(n+1):
            if i == 0 or j == 0:
                lista[i].append(0)
            else:
                lista[i].append('-')

def lcsPD(X, Y, m, n):

    b = list()
    c = list()
    iniciaMatriz(b, m, n)
    iniciaMatriz(c, m, n)

    for i in range(1, m+1):

        for j in range(1, n+1):

            if X[i-1] == Y[j-1]:

                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'd'

            elif c[i-1][j] >= c[i][j-1]:

                c[i][j] = c[i - 1][j]
                b[i][j] = 'c'

            else:

                c[i][j] = c[i][j-1]
                b[i][j] = 'e'

    return c[m][n], b

def printlcs(b, X, i, j):

    if i == 0 or j == 0:

        return

    if b[i][j] == 'd':

        printlcs(b, X, i - 1, j - 1)
        print(X[i-1], end="")

    elif b[i][j] == 'c':

        printlcs(b, X, i - 1, j)

    elif b[i][j] == 'e':

        printlcs(b, X, i, j - 1)


X = ''.join(choice('GATC') for i in range(1000))
Y = ''.join(choice('GATC') for j in range(1000))

inicio = time()
lcs, matrizprint = lcsPD(X, Y, len(X), len(Y))
final = time()

print(X)
print(Y)
print(lcs)
#printlcs(matrizprint, X, len(X), len(Y))
print(f"\n{final-inicio}")


# for x in matrizprint:
#     for i in x:
#         print(i, end = " ")
#     print()