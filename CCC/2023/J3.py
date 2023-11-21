#Special Event

ar = []
ans = []
count = []

for y in range(5):
    count.append(0)
    
    
for x in range(int(input())):
    ar.append(list(input()))

for a in range(5):
    for b in range(len(ar)):
        if ar[b][a] == "Y" and a == 0:
            count[0] += 1
        elif ar[b][a] == "Y" and a == 1:
            count[1] += 1
        elif ar[b][a] == "Y" and a == 2:
            count[2] += 1
        elif ar[b][a] == "Y" and a == 3:
            count[3] += 1
        elif ar[b][a] == "Y" and a == 4:
            count[4] += 1

for i in range(len(count)):
    if count[i] == max(count):
        ans.append(i+1)



print(','.join([str(x) for x in ans]))
