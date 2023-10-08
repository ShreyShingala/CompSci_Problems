#Which Alien?

antene = int(input("How many antennas?\n"))

eyes = int(input("How many eyes?\n"))

if antene >= 3 and eyes <= 4:
    print("TroyMartian")
if antene <= 6 and eyes >= 2:
    print("VladSaturnian")
if antene <= 2 and eyes <= 3:
    print("GraemeMercurian")
    