import random
options = ["rock", "scissors", "paper"]

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

user_choice = int(input("Welcome to the rock,scissors and paper game. Enter 0 for rock, 1 for scissor and 2 for paper \n"))

computer_choice = random.randint(0,2)

# print(f"Computer choose: {computer_choice}")

if user_choice == 0 and computer_choice == 0:
    print(f"You choose rock:{rock}")
    print (f"Computer choose rock:{rock}")
    print("The Game is draw")
elif user_choice == 1 and computer_choice == 1:
    print(f"You choose scissors:{scissors}")
    print (f"Computer choose scissors:{scissors}")
    print("The Game is draw")
elif user_choice == 2 and computer_choice == 2:
    print(f"You choose paper:{paper}")
    print (f"Computer choose paper:{paper}")
    print("The Game is draw")
elif user_choice == 0 and computer_choice == 1:
    print(f"You choose rock:{rock}")
    print (f"Computer choose scissors:{scissors}")
    print("You win")
elif user_choice == 0 and computer_choice == 2:
    print(f"You choose rock:{rock}")
    print (f"Computer choose paper:{paper}")
    print("You lose")
elif user_choice == 1 and computer_choice == 0:
    print(f"You choose scissors:{scissors}")
    print (f"Computer choose rock:{rock}")
    print("You lose")
elif user_choice == 2 and computer_choice == 1:
    print(f"You choose paper:{paper}")
    print (f"Computer choose scissors:{scissors}")
    print("You lose")
elif user_choice == 1 and computer_choice == 2:
    print(f"You choose scissors:{scissors}")
    print (f"Computer choose paper:{paper}")
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print(f"You choose paper:{paper}")
    print (f"Computer choose rock:{rock}")
    print("You win")
else:
    print("You are entering wrong number")