#Voronoi Villages

numofhomes = int(input())

smallest = float("inf")

homes = []

for i in range(numofhomes):
    homes.append(int(input()))
    
homes.sort()
for i in range(1, numofhomes - 1):
    temp = ((homes[i+1] - homes[i])/2) + ((homes[i] - homes[i-1])/2)
    if temp < smallest:
        smallest = temp
        
print(round(smallest, 1))
        
