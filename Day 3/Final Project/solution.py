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

print("Welcome the the Treasure Island")

is_Ready = input(("You are ready to hunt the treasure, Enter 'Yes' or 'No' ")).lower()

if is_Ready == "yes":
    print("You’ll face three decision points, adn your choices will decide you fate.")
    choice_1 = input("You're at the fork of the road. Choose 'left' or 'right': ")
    if choice_1 == "left":
        print("Good choice, This is the road that leads to the treasure lake!")
        choice_2 = input("You are at the lake, Decide whether you wanna 'swim' or 'wait': ")
        if choice_2 == "wait":
            print("Thanks for the patience, You have found a boat renting area nearby.")
            choice_3 = input("Bravo, You have made this far. You have given 3 doors, made the choice 'red', 'yellow', 'green', 'blue', 'white' :  ")
            if choice_3 == "red":
                print("Congrats Adventurer, You have found the treasure. A room full of expensive stone 💎and gold 🪙")
            elif choice_3 == "yellow":
                print("Yellow doesn't always represents gold, This door was a trap")
            elif choice_3 == "green":
                print("This door leads to a deadly jungle")
            elif choice_3 == "blue":
                print("Fallen from a clip of sea, You are dead.")
            elif choice_3 == "white":
                print("Good choice, you have made it to the heaven, Which mean you died peaceful, but you didn't find the treasure")
            else:
                print("You are elimenated!")
        else:
            print("Wrong choice, There are hungry crocodiles in the lake, You end up into their stomachs")
    else:
        print("You have fallen into a big hole")
else:
    print("Hope you will be ready next time")















