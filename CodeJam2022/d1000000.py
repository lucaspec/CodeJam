import numpy as np

T = int(input())

for t in range(T):
    # read and sort array
    N = int(input())
    list = [int(x) for x in input().split()]
    list = np.array(list)
    list = np.sort(list)

    # algorithm
    straight = 0
    for i in list:
        if i > straight:
            straight += 1

    print("Case #" + str(t+1) + ":", straight)
