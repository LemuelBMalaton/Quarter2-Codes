age = int(input("Hi there! Please enter your age: "))
counter = 0
sum = 0
while counter <= age - 1:
    counter += 1
    sum += counter
print("The sum of all numbers from 1 to", age, "is:", sum)
