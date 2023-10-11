# Up and Down

NikkyUp = int(input())
NikkyDown = int(input())
Nstep = 0

ByronUp = int(input())
ByronDown = int(input())
Bstep = 0

steps = int(input())


temp1 = NikkyUp
temp2 = NikkyDown

for i in range(steps):
  
    if temp1 != 0:
        Nstep += 1
        temp1 -= 1
    elif temp2 != 0:
        Nstep -= 1
        temp2 -= 1
    else:
        temp1 = NikkyUp
        temp2 = NikkyDown
        if temp1 != 0:
            Nstep += 1
            temp1 -= 1
        
temp3 = ByronUp
temp4 = ByronDown 

for i in range(steps):
    
    
    if temp3 != 0:
        Bstep += 1
        temp3 -= 1
    elif temp4 != 0:
        Bstep -= 1
        temp4 -= 1
    else:
        temp3 = ByronUp
        temp4 = ByronDown
        if temp3 != 0:
            Bstep += 1
            temp3 -= 1

if Nstep > Bstep:
    print("Nikky")
elif Nstep < Bstep:
    print("Byron")
else:
    print("Tied")