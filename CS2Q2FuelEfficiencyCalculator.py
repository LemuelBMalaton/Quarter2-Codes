def fuelefficiency(distance, fuelconsumption):
    return distance / fuelconsumption
a = int(input("Enter distance traveled (in kilometers): "))
b = int(input("Enter fuel consumed (in liters): "))
print("Fuel Efficiency:", fuelefficiency(a, b), "km/L")
    