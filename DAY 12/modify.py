enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"Enemies inside function: {enemies}")
    
increase_enemies()
print(f"Enemies outside function: {enemies}")    
    