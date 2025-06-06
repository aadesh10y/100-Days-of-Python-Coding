print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side = input("Which side do you want to go? Left or Right\n").lower()
if side != "left":
    print("You fell into a hole. Game Over.")
elif side == "left":
    lake = input("You have come to a lake. Do you wait for a boat or swim?\n").lower()
    if lake != "wait":
        print("Attacked by trout. Game Over.")
    elif lake == "wait":
        door = input("There are three doors: Blue, Red, or Yellow. Which one do you choose?\n").lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red" or door == "blue":
            print("You enter a room of fire. Game Over.")
        else:
            print("Invalid door. Game Over.")
