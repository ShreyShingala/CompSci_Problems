#Lunch Concert

#vars
bestdistance = float("inf")
mindistance = float("inf")
maxdistance = 0
speed = []
hearing = []
position = []

numofpeople = int(input())
for i in range(numofpeople):
    people = list(map(int, input().split(" ")))
    
    position.append(people[0])
    speed.append(people[1])
    hearing.append(people[2])
    if position[i] < mindistance:
        mindistance = position[i]
    if position[i] > maxdistance:
        maxdistance = position[i]

def curr_dist(point):
    global speed, hearing, position
    
    currcheck = 0
    for i in range(numofpeople):
        pos = position[i]
        sped = speed[i]
        hear = hearing[i]
        
        distance = abs(point - pos)
        
        if distance > hear:
            currcheck += (distance - hear) * sped

    return currcheck


left = mindistance
right = maxdistance
while left<=right:
    mid = (left+right)//2
    
    left_time = curr_dist(mid-1)
    currcheck = curr_dist(mid)
    right_time = curr_dist(mid+1)

    if currcheck < left_time and currcheck < right_time:
        bestdistance = currcheck
        break
    elif currcheck == left_time or currcheck == right_time:
        bestdistance = currcheck
        break
    elif currcheck <= right_time:
        right = mid-1
    else:
        left = mid +1
        

print(bestdistance)
                