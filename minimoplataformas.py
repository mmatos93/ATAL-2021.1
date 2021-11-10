def minplataformas(chegada, partida):
    #supondo que os vetores já chegam ordenados, caso contrario precisaria ordenar

    n = len(chegada)
    #e necessario pelo menos 1 plataforma inicialmente
    nplat = 1
    i, j = 0, 0

    while i < n:

        if (chegada[i] < partida[j]):
            nplat += 1
            i += 1

        else:
            nplat -= 1
            j += 1

    return nplat

#exemplo 1
chegadaex1 = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
partidaex1 = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]

print(minplataformas(chegadaex1, partidaex1))