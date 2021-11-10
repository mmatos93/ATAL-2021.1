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

def mochilaMemoizado(S, n, W, m):

    if n == 0 or W == 0:

        return 0

    if m[W][n] != '-':
        return m[W][n]

    if S[n].peso <= W:

        m[W][n] = max(S[n].valor + mochilaMemoizado(S, n-1, W-S[n].peso, m), mochilaMemoizado(S, n-1, W, m))

        return m[W][n]

    else: #if S[n].peso > W:
        m[W][n] = mochilaMemoizado(S, n-1, W, m)
        return m[W][n]


S = dict()

for i in range(1, 500):
    S[i] = ItemMochila(randint(1,6), randint(10, 15))

# S[1] = ItemMochila(6, 30)
# S[2] = ItemMochila(3, 14)
# S[3] = ItemMochila(4, 16)
# S[4] = ItemMochila(2, 9)

W = 10000
m = list()
inicio = time()
iniciaMatriz(m, len(S), W)
print(mochilaMemoizado(S, len(S), W, m))
final = time()

print(final-inicio)