import numpy as np

T = int(input())

for y in range(T):
    inputlist = input().split()
    R = int(inputlist[0])
    C = int(inputlist[1])

    print("Case #" + str(y+1) + ":" + '\n')
    for i in range(R):
        str1 = ''
        str2 = ''
        for j in range(C):
            if i == 0 and j == 0:
                str1 = '..+'
                str2 = '..|'
                continue

            if j == 0:
                str1 = '+'
                str2 = '|'

            str1 += '-+'
            str2 += '.|'
        print(str1 + '\n' + str2 + '\n')

    endstr = '+'
    for h in range(C):
        endstr += '-+'
    print(endstr)