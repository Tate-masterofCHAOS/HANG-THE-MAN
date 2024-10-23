import random

# List of words for the game
words = ["snow", "wolf", "moon", "star", "lamp"]  # Add more words as needed

# Function to display the gallows based on the number of incorrect guesses
def display_gallows(incorrect_guesses):
    layers = [
        "    ___",
        "   /   |",
        "       |",
        "       |",
        "       |",
        "       |",
        "   ---------"
    ]
    if incorrect_guesses > 0:
        layers[2] = "   O     |"  # Head
    if incorrect_guesses > 1:
        layers[3] = "  /|     |"  # Arms
    if incorrect_guesses > 2:
        layers[3] = "  /|\\    |"  # Arms
    if incorrect_guesses > 3:
        layers[4] = "  /      |"  # Body
    if incorrect_guesses > 4:
        layers[4] = "  / \\    |"  # Legs
    for layer in layers:
        print(layer)

# Main function for the Hangman game
def hangman():
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect:
        display_gallows(incorrect_guesses)
        
        # Display current state of the word
        displayed_word = "".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
        print(f"Current word: {displayed_word}")
        
        # Ask for user input
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess: {guess}")
        else:
            print(f"Sorry, {guess} is not in the word.")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"You've run out of guesses. The word was: {word_to_guess}")

# Run the game
if __name__ == "__main__":
    hangman()
