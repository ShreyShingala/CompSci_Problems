#Shifty Sum

numtoshift = int(input())
totalshift = int(input())
totalnum = numtoshift

for i in range(totalshift):
    numtoshift = int(str(numtoshift)+"0")
    totalnum += numtoshift
    
print(totalnum)