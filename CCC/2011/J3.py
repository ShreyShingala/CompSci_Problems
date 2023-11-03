#Sumac Sequences

num1 = int(input())
num2 = int(input())
sequence = []
sequence.append(num1)
sequence.append(num2)
nextnum = 0
currnum = 0
run = True

while run:
    currnum += 1
    nextnum = sequence[currnum-1] - sequence[currnum]
    if nextnum >= 0:
        sequence.append(nextnum)
    else:
        run = False
    
print(len(sequence))