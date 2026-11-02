Coffe_size = str(input("Enter the size of coffee : "))
extra_shot = bool(input("Do you want extra shot : "))

if extra_shot:
    coffee = Coffe_size + "Coffee with an Extra Shot"
else:
    coffee = Coffe_size + "Coffee"
    
print("Order: " ,coffee)