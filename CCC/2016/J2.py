#Magic Squares

line1 = list(map(int, str(input()).split(" ")))
line2 = list(map(int, str(input()).split(" ")))
line3 = list(map(int, str(input()).split(" ")))
line4 = list(map(int, str(input()).split(" ")))

number = line1[0] + line1[1] + line1[2] + line1[3]
number1 = line2[0] + line2[1] + line2[2] + line2[3]
number2 = line3[0] + line3[1] + line3[2] + line3[3]
number3 = line4[0] + line4[1] + line4[2] + line4[3]

number4 = line1[0] + line2[0] + line3[0] + line4[0]
number5 = line1[1] + line2[1] + line3[1] + line4[1]
number6 = line1[2] + line2[2] + line3[2] + line4[2]
number7 = line1[3] + line2[3] + line3[3] + line4[3]

if number == number1 == number2 == number3 == number4 == number5 == number6 == number7:
    print("magic")
else:
    print("not magic")