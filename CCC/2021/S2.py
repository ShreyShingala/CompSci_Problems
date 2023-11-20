#Modern Art TODO

row = int(input())
columns = int(input())
num = int(input())

grid = [["B"] * columns] * row

currgold = 0

print(grid)

for i in range(num):
    coords = str(input()).split(" ")
    num = int(coords[1])-1

    if coords[0] == "R":
        for i in range(columns):
            if grid[num][i] == "B":
                grid[num][i] = "G"
                currgold += 1
            elif grid[num][i] == "G":
                grid[num][i] = "B"
                currgold -= 1
                
    elif coords[0] == "C":
        for i in range(row):
            if grid[i][num] == "B":
                grid[i][num] = "G"
                currgold += 1
            elif grid[i][num] == "G":
                grid[i][num] = "B"
                currgold -= 1
                
                
    print(grid)
                
print(currgold)
            
    