#Escape Room
check = []

rows = int(input())
cols = int(input())

matrix = []
visited = [[False for i in range(cols)] for j in range(rows)]

for i in range(rows):
    matrix.append(list(map(int, input().split())))
    
firstnum = matrix[0][0]

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append([i, number // i])
            
    return factors

check.append(firstnum)

while check != []:
    
    num = check.pop(0)
    factors = find_factors(num)
    
    for i in range(len(factors)):
        num1 = factors[i][0] - 1
        num2 = factors[i][1] - 1
        if num1 < rows and num2 < cols:
            if visited[num1][num2] == False:
                check.append(matrix[num1][num2])
                visited[num1][num2] = True
                if num1 == rows - 1 and num2 == cols - 1:
                    print("yes")
                    exit(0)
    
    
print("no")
    
    
