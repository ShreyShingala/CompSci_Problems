#Speed fines are not fine!

limit = int(input("Enter the speed limit:"))
carspeed = int(input("Enter the recorded speed of the car:"))
if carspeed <= limit:
    print("Congratulations, you are within the speed limit!")
elif (carspeed - limit) >= 1 and  (carspeed - limit) <= 20:
    print("You are speeding and your fine is $100.")
elif (carspeed - limit) >= 21 and  (carspeed - limit) <= 30:
    print("You are speeding and your fine is $270.")
elif (carspeed - limit) >= 31:
    print("You are speeding and your fine is $500.")