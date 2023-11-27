#Lunch Concert

numofpeople = int(input())
people = []
bestdistance = float("inf")

for i in range(numofpeople):
    people.append(list(map(int, input().split(" "))))

people.sort(key=lambda x: int(x[0]))

lowest = people[0][0]
greatest = people[-1][0]
mid = lowest+greatest//2

def curr_dist(point):
    global people
    
    currcheck = 0
    for p in people:
        position = p[0]
        speed = p[1]
        hearing = p[2]
        
        
        if point > position:
            if (position + hearing) > point:
                continue
            else:
                currcheck += ((point - (position + hearing)) * speed)
        elif point < position:
            if (position - hearing) < point:
                continue
            else:
                currcheck += (((position - hearing)- point) * speed)
        if currcheck > bestdistance:
            break
        
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
                