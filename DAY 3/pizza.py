print("Welcome to 404 pizza Deliveries!! ")
size = input(" What size of pizza do you want? L, M or S: ")
pepperoni = input("Dou you want pepperoni or not? Y or N: ")
cheeese = input("Do you want extra cheese? Y or N: ")

price = 0
if size == "S":
    price = 15
    if pepperoni == "Y":
        price+=2
    if cheeese == "Y":
        price+=1 
    print("Your total bill is $", price)   
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price+=3
    if cheeese == "Y":
        price+=1 
    print("Your total bill is $", price)
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price+=3
    if cheeese == "Y":
        price+=1 
    print("Your total bill is $",price)
else:
    print("You are doing wrong input")
        