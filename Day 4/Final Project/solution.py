import random

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

game_figure = [rock, paper, scissors]



user_input = int(input("Choose 0 for Rock, 1 for Paper, and 2 for scissors: "))

computer_random_number = random.randint(0, 2)

users_choice = game_figure[user_input]
computer_choice = game_figure[computer_random_number]

print(f"You chose:\n{users_choice}")
print("------------&--------------")
print(f"Computer chose:\n{computer_choice}")

if users_choice == rock and computer_choice == scissors:
    print("You Win!")
elif users_choice == paper and computer_choice == rock:
    print("You Win!")
elif users_choice == scissors and computer_choice == paper:
    print("You Win 😄")
else:
    if users_choice == computer_choice:
        print("That's a Draw 🟰")
    else:
        print("Computer Wins! 💻")

