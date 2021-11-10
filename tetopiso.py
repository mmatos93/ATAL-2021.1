def buscateto(A, ini, fim, k):

    #casos base
    if(k > A[fim]):
        return -1

    if(k <= A[ini]):
        return A[ini]

    meio = (ini + fim)//2

    if(k == A[meio]):
        return A[meio]

    elif(k > A[meio]):
        return buscateto(A, meio+1, fim, k)

    else:
        return buscateto(A, ini, meio, k)

def buscapiso(A, ini, fim, k):

    #casos base
    if(k < A[ini]):
        return -1

    if(k >= A[fim]):
        return A[fim]

    meio = (ini + fim)//2

    if(ini == meio):
        return A[meio]

    if(k == A[meio]):
        return A[meio]

    elif(k > A[meio]):
        return buscapiso(A, meio, fim, k)

    else:
        return buscapiso(A, ini, meio-1, k)


A = [1, 4, 6, 8, 9]
print(A)
for k in range(0,11):
    print(k, "-> Teto: ", buscateto(A, 0, len(A)-1, k), "Piso: ", buscapiso(A, 0, len(A)-1, k))

B = [ 3, 5, 7, 10, 11, 13, 15, 16, 17, 19]
print(B)
for k in range(0,20):
    print(k, "-> Teto: ", buscateto(B, 0, len(B)-1, k), "Piso: ", buscapiso(B, 0, len(B)-1, k))