Animal_Type = str(input("Enter the type of animal : "))
age = int(input("Enter the age of Animal : "))
if Animal_Type == "Cat" and age > 5:
    print("senior cat food")
elif Animal_Type == "Dog" and age < 2:
    print("puppy food")
else:
    print("Invalid options")