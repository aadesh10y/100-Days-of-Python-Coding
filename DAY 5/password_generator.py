import random
# Alphabets (lowercase + uppercase)
alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

# Numbers
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Symbols
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
    "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<",
    ">", "?", "/", "`", "~"
]

print("Welcome to the password generator")
t_alpha = int(input("How many alphabets do you want? \n"))
t_num = int(input("How many numbers do you want? \n"))
t_sym = int(input("How many symbols do you want? \n"))

# Easy One

# password = ""
# for i in range(0,t_alpha):
#     password += random.choice(alphabets)

# for i in range(0,t_num):
#     password += random.choice(numbers)
    
# for i in range(0,t_sym):
#     password += random.choice(symbols)
# print(password)    

# Hard one 

# password_list = []

# for i in range(t_alpha):
#     password_list.append(random.choice(alphabets))

# for i in range(t_num):
#     password_list.append(random.choice(numbers))

# for i in range(t_sym):
#     password_list.append(random.choice(symbols))

# random.shuffle(password_list)
# password = ''.join(password_list)
# print(password)

password_list = []
for i in range(0,t_alpha):
    password_list.append(random.choice(alphabets))

for i in range(0,t_num):
    password_list.append(random.choice(numbers))
    
for i in range(0,t_sym):
    password_list.append(random.choice(symbols))
    
random.shuffle(password_list)   

password = ""
for i in password_list:
    password+=i
print(password)