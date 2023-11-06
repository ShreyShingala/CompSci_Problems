#Boiling Water

BoilPoint = int(input())

Pressure = BoilPoint * 5 - 400

print(Pressure)

if Pressure == 100:
  print(0)
elif Pressure < 100:
  print(1)
else: 
  print(-1)
