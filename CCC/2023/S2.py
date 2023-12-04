# Symmetric Mountains, in progress
numofmountains = int(input())

listofmountains = list(map(int, input().split(" ")))

currentstring = ""

for i in range(numofmountains):
    current = float("inf")
    if i == 0:
        currentstring += "0"
    else:
        for j in range(numofmountains - i):
            temp = 0
            subset = listofmountains[j:j+i+1]
            for k in range(len(subset)//2):
                temp += abs(subset[k] - subset[-k-1])
            current = min(current, temp)

        currentstring += " " + str(current)       
        

print(currentstring)
            
        
        