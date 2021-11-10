def buscafreq(A, ini, fim, freq):

    if(A[ini] == A[fim]):

        freq[A[ini]] = fim - ini + 1

    else:

        meio = (ini + fim)//2
        buscafreq(A, ini, meio, freq)
        buscafreq(A, meio+1, fim, freq)

freqA = {}
A = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
buscafreq(A, 0, len(A)-1, freqA)
print(freqA)

freqB = {}
B = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,6,7,8]
buscafreq(B, 0, len(B)-1, freqB)
print(freqB)

freqC = {}
C = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
buscafreq(C, 0, len(C)-1, freqC)
print(freqC)