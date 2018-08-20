
A = [[1,2,3],[4,5,6]]
C = []
D = []

for i in range(len(A[0])):
    for j in range(len(A)):
        B = A[j][i]
        C.append(B)
    D.append(C)
    C = []
print(D)