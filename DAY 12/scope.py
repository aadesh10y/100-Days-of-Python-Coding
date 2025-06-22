# local scope
def drink():
    drink_strength = 2
    print(drink_strength)
    
drink()    
# print(drink_strength)

# global scope
player_health = 10

def drink():
    drink_strength = 2
    print(player_health)

print(player_health)
    
    