def conjuntominimo(n, intervalo):

    #ordenando com relação ao tf
    intervalo.sort(key=lambda h: h[1])

    A = []
    A.append(intervalo[0])
    k = 0

    for j in range(1, n-1):

        if (intervalo[j][0] >= intervalo[k][1]):

            A.append(intervalo[j])
            k = j

    minvisitas = len(A)
    horarios = [x[1] for x in A]

    return minvisitas, horarios

#teste via linha de comando
# intervalo = []
# n = int(input())
# for i in range(0, n):
#     entrada = input()
#     intervalo.append(list(map(int, entrada.split())))
#
# qtdvisitas, horariodasvisitas = conjuntominimo(n, intervalo)
# print(qtdvisitas)
# print(*horariodasvisitas)

#exemplo 1
intervaloex2 = [[1, 3], [2, 5], [3, 6]]
nex2 = len(intervaloex2)
print(conjuntominimo(nex2, intervaloex2)[0])
print(*conjuntominimo(nex2, intervaloex2)[1])

#exemplo 2
intervaloex2 = [[4,7], [1,3], [2,5], [5,6]]
nex2 = len(intervaloex2)
print(conjuntominimo(nex2, intervaloex2)[0])
print(*conjuntominimo(nex2, intervaloex2)[1])