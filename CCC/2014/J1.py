#Triangle Times

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 + num2 + num3 != 180:
    print("Error")
elif num1 == num2 and num1 == num3:
    print("Equilateral")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("Scalene")
else:
    print("Isosceles")