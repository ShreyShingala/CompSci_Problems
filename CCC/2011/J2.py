#Who Has Seen The Wind

humidity = int(input())
time = int(input())
touched = False

for i in range(time):
    temp = i + 1
    
    height = -6 * (temp*temp*temp*temp) + humidity * (temp * temp * temp) + 2 * (temp*temp) + temp
    
    if height <= 0:
        print("The balloon first touches ground at hour:")
        print(temp)
        touched = True
        break
    
if touched == False:
    print("The balloon does not touch ground in the given time.")