import random
hangman_stages = [
    """  +---+
  |   |
      |
      |
      |
      |
=========""",
    """  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

words = [
    "apple", "banana", "cherry", "elephant", "guitar", "mountain", "python",
    "notebook", "umbrella", "puzzle", "computer", "jungle", "library", "diamond",
    "ocean", "rainbow", "butterfly", "castle", "rocket", "sunflower", "dragon",
    "candle", "volcano", "garden", "horizon", "island", "jacket", "keyboard",
    "lemonade", "marathon", "necklace", "octopus", "penguin", "quartz", "robot",
    "sandwich", "telescope", "unicorn", "violin", "whistle", "xylophone", "yogurt",
    "zeppelin", "bicycle", "camera", "dolphin", "engine", "firework", "glacier",
    "harvest", "iceberg", "jungle", "kangaroo", "lantern", "meadow", "nectar",
    "orchard", "parachute", "quiver", "raincoat", "sapphire", "tornado", "umbrella",
    "vortex", "waterfall", "xenon", "yacht", "zeppelin"
]

random_word = random.choice(words)

display = ["_" for _ in random_word]
guessed_letters = []
print(display)

total_lives = 6
hangman_number = 0
print(hangman_stages[0])

game_over = False

while not game_over:
    guess = input("Enter the alphabet: ").lower()

    if guess in guessed_letters:
        print("❌ You've already guessed that letter. Try a new one.\n")

    guessed_letters.append(guess)
    if guess in random_word:
        for index in range(len(random_word)):
            letter = random_word[index]
            if letter == guess:
                display[index] = letter
    else:
        total_lives -= 1
        hangman_number += 1
        print(f"************ Lives Left {total_lives}/6 ***************")
    print(hangman_stages[hangman_number])

    print(display)
    if "_" not in display:
        game_over = True
        print("#######Congratulations 🎉! You guessed the word. You hangman is safe.########")
    elif total_lives == 0:
        game_over = True
        print("You Lose 💀")
        print(f"The random word is: {random_word}")





























