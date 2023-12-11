#Searching for Strings, works for first 3 cases, not last one

og = str(input())
length = len(og)

longstring = str(input())
currentlist = 0
currentperms = {}


for i in range(len(longstring) - length + 1):
    temp = og
    
    substring = longstring[i:i+length]

    for j in range(length):
        if substring[j] in temp:
            truetemp = substring[j]
            temp = temp.replace(truetemp, "", 1)       
        
    if temp == "" and substring not in currentperms:
        currentperms[substring] = 1
        currentlist += 1

print(currentlist)