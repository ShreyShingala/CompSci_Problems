#Missing Number
length = int(input())
listo = list(map(int, str(input()).split(" ")))
listo.sort()

if listo[-1] != length:
    print(length)
else:
    for i in range(len(listo)):
        
        if i + 1 == listo[i]:
            pass
        else:
            print(i+1)
            break