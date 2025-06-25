import random
import os

# ASCII Art for the game
art = """
 _    _ _       _                _                 
| |  | (_)     | |              | |                
| |__| |_  __ _| |__   ___  __ _| |_ ___  ___      
|  __  | |/ _` | '_ \\ / _ \\/ _` | __/ _ \\/ __|     
| |  | | | (_| | | | |  __/ (_| | ||  __/\\__ \\     
|_|  |_|_|\\__, |_| |_|\\___|\\__,_|\\__\\___||___/     
            __/ |                                 
           |___/                                  

        Guess which celebrity has
             MORE FOLLOWERS!
"""

# celebrity data
celebrities = [
    {"name": "Cristiano Ronaldo", "followers": 630_000_000, "description": "Footballer"},
    {"name": "Lionel Messi", "followers": 500_000_000, "description": "Footballer"},
    {"name": "Selena Gomez", "followers": 430_000_000, "description": "Singer/Actress"},
    {"name": "Dwayne Johnson", "followers": 400_000_000, "description": "Actor/Wrestler"},
    {"name": "Kylie Jenner", "followers": 400_000_000, "description": "Model/Influencer"},
    {"name": "Kim Kardashian", "followers": 360_000_000, "description": "TV Personality"},
    {"name": "Beyoncé", "followers": 320_000_000, "description": "Singer"},
    {"name": "Taylor Swift", "followers": 280_000_000, "description": "Singer"},
]

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Format celebrity output
def format_celebrity(celeb):
    return f"{celeb['name']}, a {celeb['description']}"

# Main game function
def play_game():
    score = 0
    game_continue = True
    celeb_b = random.choice(celebrities)

    while game_continue:
        celeb_a = celeb_b
        celeb_b = random.choice(celebrities)
        while celeb_b == celeb_a:
            celeb_b = random.choice(celebrities)

        clear_screen()
        print(art)
        print(f"Compare A: {format_celebrity(celeb_a)}")
        print("vs")
        print(f"Against B: {format_celebrity(celeb_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        a_followers = celeb_a["followers"]
        b_followers = celeb_b["followers"]

        correct = 'a' if a_followers > b_followers else 'b'

        if guess == correct:
            score += 1
            print(f"\n✅ Correct! Current Score: {score}")
            input("Press Enter to continue...")
        else:
            clear_screen()
            print(art)
            print(f"\n❌ Wrong! Final Score: {score}")
            print(f"{celeb_a['name']}: {a_followers:,} followers")
            print(f"{celeb_b['name']}: {b_followers:,} followers")
            game_continue = False

# Run the game
play_game()
