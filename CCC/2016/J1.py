#Tournament Selection
win = 0

for i in range(6):
    let = str(input())
    if let == "W":
        win +=1
    
if win == 0:
    print("-1")
elif win <= 2:
    print("3")
elif win <= 4:
    print("2")
else:
    print("1")