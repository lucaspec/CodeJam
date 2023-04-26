import numpy as np

T = int(input())

for x in range(T):

    string = str(input())
    res = ""

    for i in range(len(string)):

        # first number
        if i == 0:
            for j in range(int(string[i])):
                res += "("

        # last number
        if i == len(string)-1:
            res += string[i]
            for j in range(int(string[i])):
                res += ")"
            
        # any other number
        if i != len(string)-1:
            current = int(string[i])
            next = int(string[i+1])

            res += string[i]

            if current > next:
                n = current-next
                for j in range(n):
                    res += ")"

            if next > current:
                n = next-current
                for j in range(n):
                    res += "("
            
            
    print("Case #"+ str(x+1) +":", res)



