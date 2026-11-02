age = int(input("Enter the age : "))
day = str(input("Enter the day : "))

price = 12 if age >= 18 else 8
if day == " Wednesday":
    price = price - 2
print("Price for you is: ", price)

 