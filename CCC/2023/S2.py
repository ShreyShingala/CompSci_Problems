# Symmetric Mountains, in progress

numbermount = int(input())

mountlist = list(map(int, str(input()).split(" ")))

currprint = "0"
currenthighest = 0
currcropval = 0
currindex = 0

for i in range(1, numbermount):
    currcropval = i+1
    currindex = 0
    
    for j in range(len(mountlist)-currcropval):
        listy = mountlist[currindex:currcropval+currindex]
        symettry = symettry(listy)
        
        if symettry > currenthighest:
            currenthighest = symettry
            currprint += " " str(currcropval)
        
        
def symettry(listy):
    num = 0
    for i in range(len(listy//2)):
        num += listy[i] - listy[len(listy)-i-1]
    
    return num
    
        