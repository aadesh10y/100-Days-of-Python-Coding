print("Welcome to the Roller Coster")
height = float(input("Enter your height in cm: "))
bill = 0
if height >=120:
    print("You are allowed to ride")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("child ticket price is $5")
    elif age <=18:
        bill = 7
        print("youth ticket price is $7")
    elif age >=45 or age<=55:  # Logical or
        print("You don't have to pay for ticket. ")
    else:
        bill = 12
        print("adult ticket price is $12")
        
    photo = input("Do you want to take photos? y for yes and n for no: ")
    if photo == "y":
        bill+=3
        print("Your total bill is $", bill)
else:
    print("You are not allowed to ride")