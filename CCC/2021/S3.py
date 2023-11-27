#Lunch Concert

numofpeople = int(input())
people = []
bestdistance = float("inf")
mindistance = float("inf")
maxdistance = 0

for i in range(numofpeople):
    people.append(list(map(int, input().split(" "))))
    
    if people[i][0] < mindistance:
        mindistance = people[i][0]
    if people[i][0] > maxdistance:
        maxdistance = people[i][0]

mid = mindistance+maxdistance//2

def curr_dist(point):
    global people
    
    currcheck = 0
    for p in people:
        position = p[0]
        speed = p[1]
        hearing = p[2]
        
        distance = abs(point - position)
        
        if distance > hearing:
            currcheck += (distance - hearing) * speed

    return currcheck

while True:
    left = curr_dist(mid-1)
    currcheck = curr_dist(mid)
    right = curr_dist(mid+1)
    
    if currcheck < left and currcheck < right:
        bestdistance = currcheck
        break
    elif currcheck == left or currcheck == right:
        bestdistance = currcheck
        break
    elif currcheck <= right:
        mid = mid-1
    else:
        mid = mid +1
   

            

print(bestdistance)
                