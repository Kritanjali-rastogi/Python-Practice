"""Program to multiply two matrices"""



for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B[j])):
            result[i][j] += A[i][k] * B[k][j]

for r in result:

