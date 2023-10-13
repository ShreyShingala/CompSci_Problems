# Rotating letters

word = str(input())
printyes = True

def check_letters(letter):
    if letter != "I" and letter != "O" and letter != "S" and letter != "Z" and letter != "X" and letter != "H" and letter != "N":
        return False
    else:
        return True
    
for chr in word:
    answ = check_letters(chr)
    if answ == False:
        print("NO")
        printyes = False
        break
    
if printyes == True:
    print("YES")