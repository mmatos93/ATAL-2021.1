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

def lcsMemoizado(X, Y, m, n, tabela):

    if m == 0 or n == 0:

        return 0

    if tabela[m][n] == '-':

        if X[m] == Y[n]:

            tabela[m][n] = lcsMemoizado(X, Y, m-1, n-1, tabela) + 1

        else:

            tabela[m][n] = max(lcsMemoizado(X, Y, m - 1, n, tabela), lcsMemoizado(X, Y, m, n - 1, tabela))

    return tabela[m][n]

X = ''.join(choice('GATC') for i in range(500))
Y = ''.join(choice('GATC') for j in range(1500))

tabela = list()
iniciaMatriz(tabela, len(X), len(Y))

print(f'Sequencia X: {X}')
print(f'Sequencia Y: {Y}')

inicio = time()
print(f"Tamanho da LCS: {lcsMemoizado(X, Y, len(X)-1, len(Y)-1, tabela)}")
final = time()

print(final-inicio)

# for x in tabela:
#     for i in x:
#         print(i, end = " ")
#     print()