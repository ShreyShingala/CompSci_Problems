#Modern Art

rows = int(input())
cols = int(input())
numlines = int(input())

col_swipes = [False] * cols
row_swipes = [False] * rows

for i in range(numlines):
    line = input().split(" ")
    index = int(line[1])-1
    if line[0] == "R":
        row_swipes[index] = not row_swipes[index]
    else:
        col_swipes[index] = not col_swipes[index]

canva = [[False for j in range(cols)] for i in range(rows)]

for i in range(cols):
    if col_swipes[i]:
        for j in range(rows):
            canva[j][i] = not canva[j][i]
            
for i in range(rows):
    if row_swipes[i]:
        for j in range(cols):
            canva[i][j] = not canva[i][j]
            
gold = 0

for i in range(rows):
    for j in range(cols):
        if canva[i][j]:
            gold += 1

print(gold)


