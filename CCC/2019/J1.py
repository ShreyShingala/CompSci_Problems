# Winning Score

A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())

A = A3 * 3 + A2 * 2 + A1
B = B3 * 3 + B2 * 2 + B1

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("T")
    