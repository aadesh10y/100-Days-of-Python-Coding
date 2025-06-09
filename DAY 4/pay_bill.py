import random

person = ["John", "Dolph", "Brock", "Jesse", "Walter"]

# 1st option
print(random.choice(person))

# 2nd option
random_person = random.randint(0,4) 
print(person[random_person])