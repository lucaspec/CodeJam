import numpy as np

# checks if a person has time for certain activity
def hasTime(person, activity):
    A = person[activity[0]:activity[1]]
    B = np.zeros(activity[1]-activity[0])
    if(np.array_equal(A,B)):
        return True
    else:
        return False

T = int(input())

for x in range(T):
    N = int(input())

    cameron = np.zeros(1440)
    jamie = np.zeros(1440)

    # read activities
    activities = []
    for i in range(N):
        activities.append(list(map(int, input().split())))

    activities = np.array(activities)
    
    # scheduling
    res = ""
    possible = True
    for i in range(N):
        if hasTime(cameron, activities[i]):
            cameron[activities[i,0]:activities[i,1]] = 1
            res += "C"
        elif hasTime(jamie, activities[i]):
            jamie[activities[i,0]:activities[i,1]] = 1
            res += "J"
        else:
            possible = False

    if not possible:
        res = "IMPOSSIBLE"

    print("Case #"+ str(x+1) +":", res)

