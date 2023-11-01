# Vote Count

number = int(input())
listy = str(input())

A = 0
B = 0

for i in range(number):
    
    if listy[i] == "A":
        A += 1
    elif listy[i] == "B":
        B += 1
        
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")