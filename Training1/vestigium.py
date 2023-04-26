import numpy as np

T = int(input())

# check if any duplicates in list
def anydup(thelist):
  seen = set()
  for x in thelist:
    if x in seen: return True
    seen.add(x)
  return False

for n in range(T):
    N = int(input())
    # read martrix
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    matrix = np.array(matrix)

    # trace
    t = np.trace(matrix)

    # check matrix
    r = 0
    c = 0
    for i in range(N):
        row = matrix[i,:]
        if anydup(row):
            r += 1
        
        column = matrix[:,i]
        if anydup(column):
            c += 1

    print("Case #"+ str(n+1) +":", t,r,c)