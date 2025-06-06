print("Welcome to the Roller Coster")
height = float(input("Enter your height in cm: "))
if height >=120:
    print("You are allowed to ride")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Your ticket price is $5")
    elif age <=18:
        print("Your ticket price is $7")
    else:
        print("Your ticket price is $12")
else:
    print("You are not allowed to ride")