#Happy or Sad

thestring = str(input())

happy = 0
sad = 0

for i in range(len(thestring)-2):
    if thestring[i] == ":":
        if thestring[i+1] == "-":
            if thestring[i+2] == "(":
                sad += 1
            elif thestring[i+2] == ")":
                happy += 1
    
if sad == 0 and happy == 0:
    print("none")            
elif sad > happy:
    print("sad")
elif sad < happy:
    print("happy")
elif sad == happy:
    print("unsure")
   