"""Program to add two matrices"""

def matrix(m,n):
    O = []
    for i in range(m):
        row=[]
        for j in range(n):
            inp = int(input(f"Enter O{[i]} {[j]}: "))
            row.append(inp)
        O.append(row)
    return O


m = int(input("Enter the number of rows of matrix: "))
n = int(input("Enter the number of columns of matrix: "))

print("Enter matrix 1")
A = matrix(m,n)
print(A)

print("Enter matrix 2")
B = matrix(m,n)
print(B)

def sum(A,B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            sum_total = (A[i][j]) + B[i][j]
            row.append(sum_total)
        output.append(row)
    return output

result = sum(A,B)

print(result)