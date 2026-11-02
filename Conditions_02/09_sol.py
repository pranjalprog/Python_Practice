Enter_year = int(input("Enter the year: "))
if Enter_year % 4 == 0 and Enter_year % 100 != 0:
    print("Leap year")
elif Enter_year % 400 == 0:
    print("Leap year")
else:
    print("Not a Leap Year")
    
    
