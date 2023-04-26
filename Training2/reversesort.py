import numpy as np

T = int(input())

for y in range(T):
    N = int(input())

    # read list
    list = []
    list = [int(x) for x in input().split()]
    list = np.array(list)

    # algorithm
    cost = 0

    for i in range(N):
        j = np.argmin(list[i:N]) + i
        sublist = np.flip(list[i:j+1])
        list[i:j+1] = sublist
        cost += j-i+1

    cost -= 1
    print("Case #" + str(y+1) + ":", cost)
