import numpy as np

N = int(input())

# read matrix
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

matrix = np.array(matrix)

# read array
a = [int(x) for x in input().split()]

# print
print("Case #" + str(y+1) + ":", cost)
