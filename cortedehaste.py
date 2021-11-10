from math import inf
from time import time
from random import randint

def cortahaste_bottomup(p, n):

    #r = {}
    r = [0]*(n+1)

    for i in range(1, n+1):

        q = -inf

        for j in range(1, i+1):

            q = max(q, p[j-1] + r[i-j])
            #print(*r)
        r[i] = q
        #print(*r)

    return q

preco = [1,5,8,9,10,17,17,20,24,30]
print(f"Valor maximo haste tamanho 4: {cortahaste_bottomup(preco, 4)}")
print(f"Valor maximo haste tamanho 2: {cortahaste_bottomup(preco, 2)}")
print(f"Valor maximo haste tamanho 10: {cortahaste_bottomup(preco, 10)}")
print(f"Valor maximo haste tamanho 7: {cortahaste_bottomup(preco, 7)}")

'''
Como a minha implementação usa duas instruções for encadeadas, cada uma delas com custo de tempo theta(n), a 
complexidade total de tempo seria dada por T(n) = theta(n^2).
'''