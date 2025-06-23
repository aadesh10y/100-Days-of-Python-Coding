# # Problem
# age = int(input("What is your age? "))
# if age < 18:
# print("You are not allowed to drive at {age}")

#Solution
try:
    age = int(input("What is your age? "))
except ValueError:
    print("You have typed an invalid number. Please type again with integer")    
    age = int(input("What is your age? "))

if age < 18:
    print(f"You are not allowed to drive at {age}")
