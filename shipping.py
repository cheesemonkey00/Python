weight = float(input("How heavy is your package: "))

#ground rates
groundflat = 20.00
twoorless = 1.50
twoto6 = 3.00
sixto10 = 4.00
morethan10 = 4.75

# Ground Shipping
print("Ground Shipping: ")
if weight <= 2:
  #print("Price : $21.50")
  print("$" + '{:.2f}'.format(groundflat + twoorless * weight))
elif weight > 2 and weight <= 6:
  #print("Price : $23.00")
  print("$" + '{:.2f}'.format(groundflat + twoto6 * weight))
elif weight > 6 and weight <= 10:
  #print("Price : $24.00")
  #weight=8.4 == 53.60
  print("$" + '{:.2f}'.format(groundflat + sixto10 * weight))
else:
  #print("Price : $24.75")
  print("$" + '{:.2f}'.format(groundflat + morethan10 * weight))

#prem ground
print("Premium Ground Shipping: ")
print("$125.00")

#drone rates
drone2 = 4.50
drone2to6 = 9.00
drone6to10 = 12.00
droneten = 14.25

print("Drone Shipping: ")
if weight <= 2:
  #print("Price : $21.50")
  print("$" + '{:.2f}'.format(drone2 * weight))
elif weight > 2 and weight <= 6:
  #print("Price : $23.00")
  print("$" + '{:.2f}'.format(drone2to6 * weight))
elif weight > 6 and weight <= 10:
  #print("Price : $24.00")
  #weight=8.4 == 53.60
  print("$" + '{:.2f}'.format(drone6to10 * weight))
else:
  #print("Price : $24.75")
  print("$" + '{:.2f}'.format(droneten * weight))
