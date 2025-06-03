# Small Coding Challenge:
# Write a Python program that:
#
# Imports the random module
#
# Creates a list of your favorite fruits (at least 5)
#
# Prints two different random fruits from the list using appropriate functions from random
# (Hint: Use either random.sample or combine random.choice smartly)

























import random

fav_fruits = ["Watermelon", "Grapes", "Banana", "Kiwi", "Pineapple", "Mango"]

random_sample = random.sample(fav_fruits, 2)

print(random_sample)