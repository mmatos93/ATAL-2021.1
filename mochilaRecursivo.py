from item import ItemMochila
from random import randint
from time import time


def mochilaRecursivo(S, n, W):
    # caso base: se não houver mais itens ou a mochila estiver cheia
    if n == 0 or W == 0:

        return 0

    if S[n].peso <= W:

        return max(S[n].valor + mochilaRecursivo(S, n-1, W-S[n].peso), mochilaRecursivo(S, n-1, W))

    else:

        return mochilaRecursivo(S, n-1, W)

S = dict()

for i in range(1, 100):
    S[i] = ItemMochila(randint(1,6), randint(10, 15))

# S[1] = ItemMochila(6, 30)
# S[2] = ItemMochila(3, 14)
# S[3] = ItemMochila(4, 16)
# S[4] = ItemMochila(2, 9)

inicio = time()
print(mochilaRecursivo(S, len(S), 10))
final = time()

print(final-inicio)