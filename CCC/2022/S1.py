# Good Fours and Good Fives

numtoget = int(input())
curnum = 0
waystomake = 0

index = 0
first4 = True
Stop = True

while Stop:  
    if first4 == True:
        if numtoget % 4 == 0:
            index = numtoget//4
            first4 = False
            waystomake += 1
                    
        else:
            first4 = False
            index = (numtoget//4) + 1
        
    for i in range(index):
        
        if (numtoget-(i*4))%5 == 0:

            waystomake += 1
            
    Stop = False 
    break
    
    

print(waystomake)
                