# Good Samples, only subtask 1 and 2

specs = str(input()).split(" ")

num = int(specs[0])
highest = int(specs[1])
goodsamples = int(specs[2])

done = None
current_unique = 1
currentset = [1] * num
currentgoods = num
minus_factor = 0

def impossible():
    print(-1)
def possible():
    global done
    print(" ".join(map(str, currentset)))
    done = True
    
if highest == 2:
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
else:
    for i in range(1, num):
        
        current_unique += 1
        temp = ((current_unique-minus_factor)*(current_unique - minus_factor + 1))//2 - current_unique + minus_factor
        
        if goodsamples == currentgoods:
            break 
        if (goodsamples-1) == currentgoods:
            currentset[num-1] = num
            currentgoods += 1
            break
        elif currentgoods + temp < goodsamples:
            currentset[i] = current_unique
        elif currentgoods + temp > goodsamples:
            print("MORE")
            
            currentgoods += ((current_unique-minus_factor-1)*(current_unique - minus_factor))//2 - current_unique + minus_factor
            currentset[i] = current_unique -1
            minus_factor = current_unique -1
            temp = 0
            
        print("CURR SET")
        print(currentset)
        print("Current good samples" + str(currentgoods))
        print("The temporary goods" + str(temp))
        
print(currentset)      
            

if currentgoods == goodsamples:
    possible()    
else:
    impossible()
    
    
