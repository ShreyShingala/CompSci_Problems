#Time to Decompress

totalprints = int(input())
thelist = []

for i in range(totalprints):
    theinput = str(input()).split(" ")
    thelist.append(theinput[1]*int(theinput[0]))
    
for i in range(len(thelist)):
    print(thelist[i])
    

    

    