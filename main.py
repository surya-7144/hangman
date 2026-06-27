import random
from words import words

HANGMAN = [
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


def play_game():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("🎮 WELCOME TO HANGMAN 🎮")
    print("=" * 40)

    while True:

        print(HANGMAN[wrong_guesses])

        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("Word:", display)
        print()

        if "_" not in display:
            print("🎉 Congratulations! You guessed the word!")
            break

        print("Guessed Letters:", " ".join(guessed_letters))
        print(f"Lives Left: {max_wrong - wrong_guesses}")

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print("❌ Wrong!")

        if wrong_guesses == max_wrong:
            print(HANGMAN[wrong_guesses])
            print("💀 GAME OVER!")
            print("The word was:", word)
            break


while True:
    play_game()

    choice = input("\nPlay Again? (y/n): ").lower()

    if choice != "y":
        print("\nThanks for playing!")
        break