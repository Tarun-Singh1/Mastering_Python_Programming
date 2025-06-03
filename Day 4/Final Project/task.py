# 🎮 Rock, Paper, Scissors Game — with ASCII Art
# This project uses everything we've learned today:
#
# random module
#
# lists
#
# error handling with IndexError
#
# ✅ Project Features:
# User chooses rock, paper, or scissors by entering 0, 1, or 2
#
# Computer randomly chooses one
#
# ASCII art is displayed for both
#
# Winner is declared (or a draw)
#
# Handles invalid user input gracefully
#
# 🧠 Step-by-Step Plan:
# Define the ASCII art for rock, paper, and scissors
#
# Store them in a list (to access by index)
#
# Get user input (0, 1, or 2)
#
# Use random.randint() to get computer's choice
#
# Compare user and computer choice
#
# Print the result
#
# Handle IndexError if user enters invalid number



# ASCII Art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
