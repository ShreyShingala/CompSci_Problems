stringy = str(input())
stringy = stringy[2:-2]
stringy = stringy.split("],[")

for i in range(len(stringy)):
    print(stringy[i][0] + " " + stringy[i][2])

