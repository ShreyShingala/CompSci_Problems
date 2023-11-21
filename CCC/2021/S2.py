#Modern Art - TO SLOW

row = int(input())
columns = int(input())
num = int(input())

grid = [[0] * columns for _ in range(row)]

currgold = 0

for _ in range(num):
    coords = str(input()).split(" ")
    index = int(coords[1])-1

    if coords[0] == "R":
        for j in range(columns):
            if grid[index][j] == 0:
                grid[index][j] = 1
                currgold += 1
            else:
                grid[index][j] = 0
                currgold -= 1
                
    elif coords[0] == "C":
        for j in range(row):
            if grid[j][index] == 0:
                grid[j][index] = 1
                currgold += 1
            else:
                grid[j][index] = 0
                currgold -= 1
    
print(currgold)

