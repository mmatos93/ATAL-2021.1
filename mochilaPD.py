from item import ItemMochila
from random import randint
from time import time

def iniciaMatriz(m, n, W):
    for i in range(W+1):
        m.append(list())
        for j in range(n+1):
            if i == 0 or j == 0:
                m[i].append(0)
            else:
                m[i].append('-')

def mochila(S=dict(), n=0, W=0):
    m = list()
    iniciaMatriz(m, n, W)
    for i in range(1, n+1):
        for w in range(1, W+1):
            if S[i].peso > w:
                m[w][i] = m[w][i-1]
            else:
                m[w][i] = max(m[w-S[i].peso][i-1] + S[i].valor, m[w][i-1])

    return m[W][n]

S = dict()

for i in range(1, 500):
    S[i] = ItemMochila(randint(1,6), randint(10, 15))

inicio = time()
print(mochila(S, len(S), 10000))
final = time()

print(final-inicio)