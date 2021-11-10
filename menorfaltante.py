def menorfaltante(A, ini, fim):

    #caso base
    if (ini > fim):

        return ini

    meio = (ini + fim)//2

    if (A[meio] == meio):

        return menorfaltante(A, meio+1, fim)

    else:

        return menorfaltante(A, ini, meio-1)


A = [0, 1, 2, 6, 9, 11, 15]
print("A = ", A, "Res = ", menorfaltante(A, 0, len(A)-1))

B = [1, 2, 3, 4, 6, 9, 11, 15]
print("B = ", B, "Res = ", menorfaltante(B, 0, len(B)-1))

C = [0, 1, 2, 3, 4, 5, 6, 8]
print("C = ", C, "Res = ", menorfaltante(C, 0, len(C)-1))