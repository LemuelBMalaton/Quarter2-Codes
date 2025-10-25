def deliveryfee(a, b):
    return a * b

distance = int(input("Enter distance in kilometers: "))
rate = int(input("Enter rate per kilometer (₱): "))

print("Total Delivery Fee: ₱" + str(f"{deliveryfee(distance, rate):.2f}"))