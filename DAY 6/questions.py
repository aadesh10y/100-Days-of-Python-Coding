#  Print Even Numbers from 2 to 10
i = 2
while i <= 10:
    print(i)
    i += 2

# Countdown from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1

# Sum of First 10 Natural Numbers
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum:", total)

# Ask Until Correct Password
password = ""
while password != "secret123":
    password = input("Enter password: ")
    if password != "secret123":
        print("Wrong password. Try again.")
print("Access granted.")

