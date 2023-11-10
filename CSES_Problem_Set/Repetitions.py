#Repetitions

listofchar = list(input())
highest = 1
currentseq = 0
currentchar = ""
for i in range(len(listofchar)-1):

    if listofchar[i] == listofchar[i+1]:
        if listofchar[i] != currentchar:
            currentseq += 2
            currentchar = listofchar[i]
        else:
            currentseq += 1
            
        if currentseq > highest:
            highest = currentseq
            currentchar = listofchar[i]

    else:
        currentseq = 0
        currentchar = listofchar[i]
    
        

if currentseq > highest:
    highest = currentseq

print(highest)