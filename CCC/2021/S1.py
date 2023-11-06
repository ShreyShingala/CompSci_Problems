#Crazy Fencing

totalshapes = int(input())
sidelist = list(map(int, str(input()).split(" ")))
baselist = list(map(int, str(input()).split(" ")))

total = 0

for i in range(totalshapes):
    left = sidelist[i]
    right = sidelist[i + 1]
    base = baselist[i]
    
    total += (left+right)*base/2
    
total = str(total)
if total[-2:] == ".0":
    print(total[:-2])
else:
    print(total)
    

    