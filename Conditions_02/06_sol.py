Distance = int(input("Enter the Distance"))
if Distance < 3:
    print("Walk")
elif Distance < 15:
    print("Bike")
else:
    print("Car")