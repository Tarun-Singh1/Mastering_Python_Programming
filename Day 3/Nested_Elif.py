# 🧩 Challenge: Weather Checker
# Create a program that checks the weather condition and gives an appropriate message.
#
# 🔨 Your Task:
# Ask the user to input a weather condition: "sunny", "rainy", or "snowy".
#
# Use if, elif, and else to print:
#
# "Wear sunglasses!" if it's sunny
#
# "Don't forget an umbrella!" if it's rainy
#
# "Stay warm with a coat!" if it's snowy
#
# "I don't know that weather." for anything else

#---------------Solution Below -----------------#

























weather = input("Please input your weather condition: ")

if weather == "sunny":
    print("Wear sunglasses!")
elif weather == "rainy":
    print("Don't forget an umbrella!")
elif weather == "snowy":
    print("Stay warm with a coat!")
else:
    print("I don't know that weather.")