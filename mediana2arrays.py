from statistics import median

def mediana2arrays(A, B, n):

    #caso array vazio
    if n == 0:
        return -1
    #caso base
    elif n == 2:
        return (max(A[0], B[0]) + min(A[1], B[1])) / 2

    else:

        med1 = median(A)
        med2 = median(B)

        if med1 > med2:

            if n % 2 == 0:

                return mediana2arrays(A[:int(n / 2) + 1], B[int(n / 2) - 1:], int(n / 2) + 1)

            else:

                return mediana2arrays(A[:int(n / 2) + 1], B[int(n / 2):], int(n / 2) + 1)

        else:

            if n % 2 == 0:

                return mediana2arrays(A[int(n / 2) - 1:], B[:int(n / 2) + 1], int(n / 2) + 1)

            else:

                return mediana2arrays(A[int(n / 2):], B[:int(n / 2) + 1], int(n / 2) + 1)

n = int(input())

entrada = input()
arrayA = list(map(int, entrada.split()))

entrada = input()
arrayB = list(map(int, entrada.split()))

print(mediana2arrays(arrayA, arrayB, n))