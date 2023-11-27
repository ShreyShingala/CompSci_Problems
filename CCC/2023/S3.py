#Palindromic Poster
done = False
def change_alphabet(alpha):
    if alpha == None:
        return "a"
    if alpha == "a":
        return "b"
    if alpha == "b":
        return "c"
    if alpha == "c":
        return "d"
    if alpha == "d":
        return "e"
    if alpha == "e":
        return "f"
    if alpha == "f":
        return "g"
    if alpha == "g":
        return "h"
    if alpha == "h":
        return "i"
    if alpha == "i":
        return "j"
    if alpha == "j":
        return "k"
    if alpha == "k":
        return "l"
    if alpha == "l":
        return "m"
    if alpha == "m":
        return "n"
    if alpha == "n":
        return "o"
    if alpha == "o":
        return "p"
    if alpha == "p":
        return "q"
    if alpha == "q":
        return "r"
    if alpha == "r":
        return "s"
    if alpha == "s":
        return "t"
    if alpha == "t":
        return "u"
    if alpha == "u":
        return "v"
    if alpha == "v":
        return "w"
    if alpha == "w":
        return "x"
    if alpha == "x":
        return "y"
    if alpha == "y":
        return "z"
    if alpha == "z":
        return None

def print_poster():
    for i in range(Rows):
        for j in range(Cols):
            print(poster[i][j], end="")
        print()

def give_up():
    global done
    print('IMPOSSIBLE')
    done = True
    
stringy = str(input()).split(" ")

Rows = int(stringy[0])
Cols = int(stringy[1])
RowPal = int(stringy[2])
ColPal = int(stringy[3])

poster = [["a"] * Cols for i in range(Rows)]

RowList = [True] * RowPal + [False] * (Rows - RowPal)
ColList = [True] * ColPal + [False] * (Cols - ColPal)

for i in range(Rows):
    if not RowList[i]:
        poster[i][-1] = change_alphabet(poster[i][-1])
    
for j in range(Cols):
    if not ColList[j]:
        poster[-1][j] = change_alphabet(poster[-1][j])
        
for i in range(Rows):
    if RowList[i]:
        temp = poster[i]
        temp.reverse()
        
        if temp != poster[i]:
            give_up()
            break
    

if not done:
    for i in range(Cols):
        if ColList[i]:
            temp = []
            for j in range(Rows):
                temp.append(poster[j][i])
            temp.reverse()
            
            if temp != poster[i]:
                give_up()
                break
    
if not done:
    print_poster()
