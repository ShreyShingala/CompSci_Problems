#Lunch Concert

numofpeople = int(input())
people = []
bestdistance = float("inf")

for i in range(numofpeople):
    people.append(list(map(int, input().split(" "))))

people.sort(key=lambda x: int(x[0]))

lowest = people[0][0]
greatest = people[-1][0]

for i in range(lowest, greatest+1):
    currcheck = 0
    for p in people:
        position = p[0]
        speed = p[1]
        hearing = p[2]
        if i > position:
            if (position + hearing) > i:
                continue
            else:
                currcheck += ((i - (position + hearing)) * speed)
        elif i < position:
            if (position - hearing) < i:
                continue
            else:
                currcheck += (((position - hearing)- i) * speed)
            
        
    bestdistance = min(currcheck, bestdistance)
            

print(bestdistance)
                