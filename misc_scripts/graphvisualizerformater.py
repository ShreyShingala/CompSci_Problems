stringy = str(input())
stringy = stringy[2:-2]
#[[1,3],[3,4],[1,5],[3,5],[2,3]]
stringy = stringy.split("],[")

for i in range(len(stringy)):
    print(stringy[i][0] + " " + stringy[i][2])

