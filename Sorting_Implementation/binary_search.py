#binary search
sortlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


a = 0
b = len(sortlist)-1

numtofind = int(input("What number do you want to find?"))

while a<=b:
    k = (a+b)//2
    if sortlist[k] == numtofind:
        print("Found it")
        print(numtofind)
        print("________________________")
        print(k)
        break

    if sortlist[k] > numtofind:
        b = k-1
    else:
        a = k+1