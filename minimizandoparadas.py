def minParadas(destino, disttanquecheio, nparadas, posicao):

    nabastecimentos = 0
    paradaatual = 0
    #a distancia que posso percorrer inicialmente é igual a distancia com o tanque cheio
    distpossivel = disttanquecheio

    #enquanto ainda não conseguir chegar ao destino, executa o loop
    while distpossivel < destino:

        #verifica se posso chegar até o proximo posto sem abastecer
        while (paradaatual < nparadas - 1 and posicao[paradaatual + 1] <= distpossivel):

            paradaatual += 1

        #se não conseguir chegar até o destino ou até um posto mais próximo, retorna -1
        if (paradaatual >= nparadas or posicao[paradaatual] > distpossivel):

            return -1

        #considerando que enche o tanque até o maximo sempre que parar
        distpossivel = disttanquecheio + posicao[paradaatual]
        nabastecimentos += 1
        paradaatual += 1

    return nabastecimentos

# teste via linha de comando
# D = int(input())
# m = int(input())
# n = int(input())
# postos = input()
# paradas = list(map(int, postos.split()))
#
# print(minParadas(D, m, n, paradas))

#teste 1
D = 950
m = 400
n = 4
paradas = [200, 375, 550, 750]
print(minParadas(D, m, n, paradas))

#teste 2
D = 10
m = 3
n = 4
paradas = [1, 2, 5, 9]
print(minParadas(D, m, n, paradas))