import random

def choose_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy (Number between 1-10, 5 attempts)")
    print("2. Medium (Number between 1-50, 7 attempts)")
    print("3. Hard (Number between 1-100, 10 attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            return (1, 10, 5)
        elif choice == '2':
            return (1, 50, 7)
        elif choice == '3':
            return (1, 100, 10)
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    lower, upper, max_attempts = choose_difficulty()
    secret_number = random.randint(lower, upper)
    attempts = 0

    print(f"\nGuess the number between {lower} and {upper}. You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if guess < lower or guess > upper:
            print(f"⚠️ Your guess must be between {lower} and {upper}. Try again.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try a higher number.")
        else:
            print("📈 Too high! Try a lower number.")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"🔁 Attempts left: {remaining}\n")
        else:
            print(f"\n💥 Game Over! The correct number was {secret_number}.")

if __name__ == "__main__":
    play_game()
