# Good Samples, only subtask 1 and 2

specs = str(input()).split(" ")

num = int(specs[0])
highest = int(specs[1])
goodsamples = int(specs[2])

done = None
currentset = [1] * num
currentgoods = num

def impossible():
    print(-1)
    
def possible():
    global done
    print(" ".join(map(str, currentset)))
    done = True
    

for i in range(1, num, 2):
    if currentgoods < goodsamples:
        if (goodsamples-1) == currentgoods:
            if currentset[num-2] == 1 and currentset[num-1] != 2:
                currentset[num-1] = 2 
                currentgoods += 1
                break
            elif currentset[num-2] == 2 and currentset[num-1] != 1:
                currentset[num-1] = 1
                currentgoods += 1
                break    
        else:
            if i == num-1:
                currentset[i] = 2
                currentgoods += 1
            else:
                currentset[i] = 2
                currentgoods += 2

    elif currentgoods > goodsamples:
        break
    
    if currentgoods == goodsamples:
        break


if currentgoods == goodsamples:
    possible()    
else:
    impossible()