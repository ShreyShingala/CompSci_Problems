#Punchy

A = 0
B = 0
run = True

while run:
    card = str(input())
    card = card.split(" ")
    
    if str(card[0]) == "1":
        if str(card[1]) == "A":
            A = int(card[2])
        else: 
            B = int(card[2])
        
    if str(card[0]) == "2":
        if str(card[1]) == "A":
            print(A)
        else: 
            print(B)
            
    if str(card[0]) == "3":
        if str(card[1]) == "A" and str(card[2]) == "A":
            A = A + A
        elif str(card[1]) == "A" and str(card[2]) == "B":
            A = A + B
        elif str(card[1]) == "B" and str(card[2]) == "B":
            B = B + B
        elif str(card[1]) == "B" and str(card[2]) == "A":
            B = B + A
            
    if str(card[0]) == "4":
        if str(card[1]) == "A" and str(card[2]) == "A":
            A = A * A
        elif str(card[1]) == "A" and str(card[2]) == "B":
            A = A * B
        elif str(card[1]) == "B" and str(card[2]) == "B":
            B = B * B
        elif str(card[1]) == "B" and str(card[2]) == "A":
            B = B * A
        
    if str(card[0]) == "5":
        
        if str(card[1]) == "A" and str(card[2]) == "A":
            A = A - A
        elif str(card[1]) == "A" and str(card[2]) == "B":
            A = A - B
        elif str(card[1]) == "B" and str(card[2]) == "B":
            B = B - B
        elif str(card[1]) == "B" and str(card[2]) == "A":
            B = B - A
        
    if str(card[0]) == "6":
       
        if str(card[1]) == "A" and str(card[2]) == "A":
            if A<0:
                A = abs(abs(A)//abs(A))
            else:
                A = (A//A)
            
        elif str(card[1]) == "A" and str(card[2]) == "B":
            if A < 0 and B <0:
                A = abs(abs(A)//abs(B))
            elif A > 0 and B > 0:
                A = abs(abs(A)//abs(B))
            else:
                A = -abs(abs(A)//abs(B))
        elif str(card[1]) == "B" and str(card[2]) == "B":
            if B<0:
                B = abs(abs(B)//abs(B))
            else:
                B = B//B
        elif str(card[1]) == "B" and str(card[2]) == "A":
            if A < 0 and B <0:
                B = abs(abs(B)//abs(A))
            elif A > 0 and B > 0:
                B = abs(abs(B)//abs(A))
            else:
                B = -abs(abs(B)//abs(A))
        
        print(A)
        print(B)
        
    if str(card[0]) == "7":
        run = False