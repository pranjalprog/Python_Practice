Enter_password = str(input("Enter the password : "))
if len(Enter_password) < 6:
    print("weak Password")
elif len(Enter_password) < 10:
    print("Medium Password")
else:
    print("Strong Password")