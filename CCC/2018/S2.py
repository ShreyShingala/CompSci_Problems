#Sunflowers

numsun = int(input())

rotation = 360

sunbed = []

for i in range(numsun):
    sunbed.append(list(map(int, input().split())))
    
    
def check_height(num):
    global sunbed, numsun
    
    if num == 0:
        for i in range(numsun):
            for j in range(numsun-1):
                if sunbed[i][j] > sunbed[i][j + 1]:
                    return False
        return True

    if num == 1:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[j][i] > sunbed[j + 1][i]:
                    return False
        return True
        
    if num == 2:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[i][j] < sunbed[i][j + 1]:
                    return False
        return True
    if num == 3:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[j][i] < sunbed[j + 1][i]:
                    return False
        return True
def check_updown(num):
    global sunbed, numsun
    
    if num == 0:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[j][i] > sunbed[j + 1][i]:
                    return False
        return True
        
    if num == 1:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[i][j] < sunbed[i][j + 1]:
                    return False
        return True
        
    if num == 2:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[j][i] < sunbed[j + 1][i]:
                    return False
        return True
        
    if num == 3:
        for i in range(numsun):
            for j in range(numsun -1):
                if sunbed[i][j] > sunbed[i][j + 1]:
                    return False
        return True
    
for i in range(4):
    
    if check_height(i):
        if check_updown(i):
            break
    
    rotation -= 90
        
if rotation == 360:
    for i in range(numsun):
        for j in range(numsun):
            print(sunbed[i][j], end = " ")
        print()

if rotation == 90:
    for i in range(numsun):
        for j in range(numsun -1, -1, -1):
            print(sunbed[j][i], end = " ")
        print()
        
if rotation == 180:
    for i in range(numsun -1, -1, -1):
        for j in range(numsun -1, -1, -1):
            print(sunbed[i][j], end = " ")
        print()
        
if rotation == 270:
    for i in range(numsun -1, -1, -1):
        for j in range(numsun):
            print(sunbed[j][i], end = " ")
        print()
    
    
    

