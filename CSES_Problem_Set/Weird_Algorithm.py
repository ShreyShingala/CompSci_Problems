#Weird Algorithm


number = int(input())
total_string = str(number)

while True:
    if number%2 == 0:
        number = number//2
        total_string += " " + str(number)
    elif number == 1:
        number = number//2
        break
    else:
        number = number*3 + 1
        total_string += " " + str(number)
        
print(total_string)