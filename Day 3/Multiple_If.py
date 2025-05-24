# 🧩 Challenge: Fitness Tracker
# Write a program that checks three conditions and responds accordingly.
#
# 🔨 Your Task:
# Ask the user three questions (yes/no answers):
#
# "Did you sleep 8 hours?"
#
# "Did you drink enough water?"
#
# "Did you exercise today?"
#
# Use three independent if statements to print feedback:
#
# If yes to sleep → "Great job sleeping well!"
#
# If yes to water → "Hydration is key!"
#
# If yes to exercise → "Keep up the good work!"
#
# Even if all three answers are "yes", all three messages should be printed.



#---------------Solution Below -----------------#




















question1 = input("Did you sleep 8 hours?")
question2 = input("Did you drink enough water?")
question3 = input("Did you exercise today?")

if question1 == "yes":
    print("Great job sleeping well!")
else:
    print("Try to sleep well!")

if question2 == "yes":
    print("Hydration is key!")
else:
    print("Drink Water")

if question3 == "yes":
    print("Keep up the good work!")
else:
    print("It is essential, so at least try to do exercise thrive in a week")
