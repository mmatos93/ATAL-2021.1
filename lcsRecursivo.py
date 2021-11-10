from random import choice, randint
from time import time

def lcsRecursivo(X, Y, m, n):
    # caso base: recursão chegou ao final das subsequencias
    if m == 0 or n == 0:

        return 0

    if X[m] == Y[n]:

        return lcsRecursivo(X, Y, m-1, n-1) + 1

    return max(lcsRecursivo(X, Y, m-1, n), lcsRecursivo(X, Y, m, n-1))


X = ''.join(choice('GATC') for i in range(100))
Y = ''.join(choice('GATC') for j in range(100))
# X = ''.join(choice('GATC') for i in range(randint(1, 25)))
# Y = ''.join(choice('GATC') for j in range(randint(1, 25)))

print(f'Sequencia X: {X}')
print(f'Sequencia Y: {Y}')
inicio = time()
print(f"Tamanho da LCS: {lcsRecursivo(X, Y, len(X)-1, len(Y)-1)}")
final = time()

print(final-inicio)