import numpy as np

T = int(input())

for x in range(T):
    # read printer matrix
    matrix = []
    for i in range(3):
        matrix.append(list(map(int, input().split())))
    matrix = np.array(matrix)

    c = np.amin(matrix[:,0])
    m = np.amin(matrix[:,1])
    y = np.amin(matrix[:,2])
    k = np.amin(matrix[:,3])

    if c+m+y+k < 1000000:
        print("Case #" + str(x+1) + ":", "IMPOSSIBLE")
    else:
        if c >= 1000000:
            print("Case #" + str(x+1) + ":", str(1000000), 0, 0, 0)
        elif c+m >= 1000000:
            print("Case #" + str(x+1) + ":", str(c), str(1000000-c), 0, 0)
        elif c+m+y >= 1000000:
            print("Case #" + str(x+1) + ":", str(c), str(m), str(1000000-c-m), 0)
        elif c+m+y+k >= 1000000:
            print("Case #" + str(x+1) + ":", str(c), str(m), str(y), str(1000000-c-m-y))