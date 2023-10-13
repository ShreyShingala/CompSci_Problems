# Sounds fishy!

reading = []
for i in range(4):
    reading.append(int(input()))
    
totalreadings = len(reading)
rise = 0
fall = 0
same = 0
    
for i in range (totalreadings - 1):
    if reading[i] > reading[i + 1]:
        rise += 1
    if reading[i] < reading[i + 1]:
        fall += 1
    if reading[i] == reading[i + 1]:
        same += 1
        
if rise == totalreadings - 1:
    print("Fish Diving")
elif fall == totalreadings - 1:
    print("Fish Rising")
elif same == totalreadings - 1:
    print("Constant Depth")
else:
    print("No Fish")