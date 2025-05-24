

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/_______/
/______/______/______/__"=._o--._   ;o|o;     _._;o;_____/______/______/____/
/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_____/
*******************************************************************************
''')

from colorama import init, Fore, Style
init()  # Initialize colorama

print(Fore.CYAN + "Welcome to the Treasure Island! 🏝️" + Style.RESET_ALL)

is_Ready = input(Fore.YELLOW + "Are you ready to hunt the treasure? Enter 'Yes' or 'No': " + Style.RESET_ALL).lower()

if is_Ready == "yes":
    print(Fore.GREEN + "🎮 You'll face three decision points, and your choices will decide your fate! 🎲" + Style.RESET_ALL)
    choice_1 = input(Fore.YELLOW + "You're at the fork of the road. Choose 'left' or 'right': 🔀 " + Style.RESET_ALL).lower()
    if choice_1 == "left":
        print(Fore.GREEN + "Good choice! 🌟 This is the road that leads to the treasure lake! 🌊" + Style.RESET_ALL)
        choice_2 = input(Fore.YELLOW + "You are at the lake. Decide whether you want to 'swim' or 'wait': 🏊‍♂️ " + Style.RESET_ALL).lower()
        if choice_2 == "wait":
            print(Fore.GREEN + "Thanks for the patience! ⏳ You have found a boat renting area nearby! ⛵" + Style.RESET_ALL)
            choice_3 = input(Fore.YELLOW + "Bravo! You've made it this far! 🎉 You see 3 doors. Choose 'red', 'yellow', or 'green', blue, white: 🚪 " + Style.RESET_ALL).lower()
            if choice_3 == "red":
                print(Fore.CYAN + "🎊 CONGRATULATIONS ADVENTURER! 🎊" + Style.RESET_ALL)
                print(Fore.GREEN + "You have found the treasure! A room full of expensive stones 💎 and gold 🪙" + Style.RESET_ALL)
            elif choice_3 == "yellow":
                print(Fore.RED + "Yellow doesn't always represent gold! This door was a trap! 💀" + Style.RESET_ALL)
            elif choice_3 == "green":
                print(Fore.RED + "This door leads to a deadly jungle! 🌴☠️" + Style.RESET_ALL)
            elif choice_3 == "blue":
                print(Fore.RED + "You've fallen from a cliff into the sea! You are dead! 🌊💀" + Style.RESET_ALL)
            elif choice_3 == "white":
                print(Fore.BLUE + "Good choice! You've made it to heaven 👼, which means you died peacefully, but didn't find the treasure!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "You are eliminated! ❌" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Wrong choice! There are hungry crocodiles in the lake! 🐊 You end up in their stomachs! ☠️" + Style.RESET_ALL)
    else:
        print(Fore.RED + "You have fallen into a big hole! 🕳️ Game Over! ☠️" + Style.RESET_ALL)
else:
    print(Fore.YELLOW + "Hope you will be ready next time! 👋" + Style.RESET_ALL)