import numpy as np

T = int(input())

for o in range(T):
    # read input
    inputlist = input().split(' ')
    x = int(inputlist[0])
    y = int(inputlist[1])
    string = str(inputlist[2])
    
    if len(string) == 1:
        print("Case #" + str(o+1) + ":", str(0))
        continue
        

    # generate minimal cost string
    new_string = ''
    i = 0
    flag = False
    while i < len(string):
        
        # first letter
        if i == 0 and string[i] == '?':
            count = 0
            # count number of starting '?'
            for j in range(len(string)):
                if count == len(string):
                    flag = True
                if string[j] == '?':
                    count += 1
                else:
                    letter = string[j]
                    break

            if string[i+1] == 'C':
                new_string += 'C'
            if string[i+1] == 'J':
                new_string += 'J'

            # case if string starts with multiple '?'
            else:
                if count != len(string):
                    for j in range(count):
                        new_string += letter
                i = count-1

        elif i == 0:
            if string[i] == 'C':
                new_string += 'C'
            if string[i] == 'J':
                new_string += 'J'

        # any other case
        else:
            if string[i] == '?':
                new_string += new_string[i-1]
            else:
                new_string += string[i]

        # increment
        i += 1

    # easiest solution
    #new_string=string.replace('?','')
    # compute cost
    cost = 0
    for i in range(len(new_string)-1):
        if flag:
            cost = 0
        if new_string[i] == 'C' and new_string[i+1] == 'J':
            cost += x
        if new_string[i] == 'J' and new_string[i+1] == 'C':
            cost += y

    print("Case #" + str(o+1) + ":", cost, new_string)
