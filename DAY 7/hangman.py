import random

stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

#  Get difficulty level
def get_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (8 lives)")
    print("2. Medium (6 lives)")
    print("3. Hard (4 lives)")
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == '1':
            return 8
        elif choice == '2':
            return 6
        elif choice == '3':
            return 4
        else:
            print("❌ Invalid choice. Please choose 1, 2 or 3.")

#  Load words from file
def load_words(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print("❌ words.txt not found. Using default word list.")
        return ["python", "hangman", "giraffe", "elephant"]

#  Main game logic
def play_game():
    wordlist = load_words()
    chosen_word = random.choice(wordlist)
    word_length = len(chosen_word)
    lives = get_difficulty()
    display = ["_"] * word_length
    guessed_letters = set()
    game_over = False

    print("\n🎮 Welcome to Hangman!")
    # print(f"(DEBUG) The word is: {chosen_word}")

    while not game_over:
        print("\nWord: " + " ".join(display))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        guess = input("Guess a letter or the full word: ").lower()

        if not guess.isalpha():
            print("❌ Only letters are allowed.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that.")
            continue

        guessed_letters.add(guess)

        if len(guess) > 1:  # full word guess
            if guess == chosen_word:
                display = list(chosen_word)
                print(f"\n🎉 Correct! The word was '{chosen_word}'")
                game_over = True
            else:
                lives -= 1
                print(f"❌ Incorrect word. Lives left: {lives}")
        else:
            if guess in chosen_word:
                for i in range(word_length):
                    if chosen_word[i] == guess:
                        display[i] = guess
                print("✅ Good guess!")
            else:
                lives -= 1
                print(f"❌ '{guess}' is not in the word. Lives left: {lives}")

        # Show hangman
        stage_index = min(len(stages) - 1, len(stages) - (lives if lives >= 0 else 0) - 1)
        print(stages[stage_index])

        if "_" not in display:
            print("🎉 You guessed the word! You win!")
            game_over = True
        elif lives <= 0:
            print("💀 You ran out of lives. Game over!")
            print(f"The word was: '{chosen_word}'")
            game_over = True

#  Play again option
def main():
    while True:
        play_game()
        again = input("\n🔁 Play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
