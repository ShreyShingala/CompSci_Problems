#Good Groups, can't do the last one

#vars
together = {}
apart = {}
groups = {}
violates = 0

num_together = int(input())
violates += num_together
for i in range(num_together):
    together[i] = input().split(" ")
    
num_apart = int(input())

for i in range(num_apart):
    apart[i] = input().split(" ")
    
num_groups = int(input())

for i in range(num_groups):
    group = input().split(" ")
    

    for j in range(num_together):
        have = together[j]
        if have[0] in group and have[1] in group:
            violates -= 1
            
    for k in range(num_apart):
        apartied = apart[k]
        if apartied[0] in group and apartied[1] in group:
            violates += 1
            

print(violates)