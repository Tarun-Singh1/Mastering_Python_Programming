# 🎯 Project Goal
# Create a Silent Bid Auction program that:
#
# Allows multiple users to place a bid.
#
# Keeps all bids secret (like a silent auction).
#
# Determines who placed the highest bid at the end.
#
# Uses a dictionary to store bids with names as keys and amounts as values.
#
# 🧾 Features You’ll Build
# ✅ Ask the user for:
#
# Their name
#
# Their bid amount
#
# ✅ Store the data like this:
#
# python
# Copy
# Edit
# bids = {
#     "Alice": 100,
#     "Bob": 250
# }
# ✅ Keep asking for new bidders until someone types "no" when asked if there are more bidders.
#
# ✅ At the end, display the name and amount of the highest bidder.
#
# 🧠 Hints & Concepts to Use
# Use a while loop to keep the program running.
#
# Store the name as the key, and bid amount as the value in a dictionary.
#
# Use a function to find the highest bid and bidder.
#
# Use clear() to clear the screen (you can simulate it if you're in a browser or IDE).
#
# Convert bid amount to an integer or float before storing.
#
# Use a flag to control when the loop ends.
# Hints ⬆️☝

import random

logo = [
    '''
  "Now, this strange, though deceptively
  simple-looking Earth device is called
  a HAMMER. It's function, however, is
  more complicated than it appears...."
                __
               (_()  \\
          \\__/  ||    \\  \\__/
          (oo)  /)       (oo)
         //~~\\\\//       //~~\\\\
         \\\\__/\\/   _____\\\\__//_____
          |/\\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|____jro


8888888888888888888888888888888888888888
8888888888888888888888888888888888888888
''' ,

'''
           __      Silence, please!
          (_()  Watch very closely, now....
           ||           /
      \\__/ /)     \\__/ /
      (_o)//      (oo)
      ( \\\\/_     //~~\\\\
       \\_\\__)____\\\\__//______
       ||| |                 |
   __  ||| |                 | _______
   ___(_(_)|_________________|______jro


999999999999999999999999999999999999999
999999999999999999999999999999999999999
''',
'''


     YOMP!!
        \\
       \\__/        \\__/
       (_X)        (oo)
       (\\\\\\\\'|`/. //~~\\\\
        |\\__\\|/___\\\\__//_______
        |||/|smash!           |
   _____|||'||'.\\             |__________
  _____(_(_)|_________________|_______jro


JROJROJROJROJROJROJROJROJROJROJROJROJROJRO
JROJROJROJROJROJROJROJROJROJROJROJROJROJRO
''',
'''


               Current theories suggest that this
               incredible rite may be related to
                their mating practices, as the
               ritual has been frequently observed
  !howl!        during the construction phase of
   !howl!      their proto-fab-dwellings. And so,
    !howl!     the search for knowledge goes on...
     !howl!    __               /
         \\    (_()             /
     ` + \\__/  ||       \\__/  /
    '(*).(xx)  /)       (oo)
    + \\\\//~~\\\\//       //~~\\\\
       \\/\\__/\\/   _____\\\\__//_____
         |/\\|    |                |
   _____ |||| ___|                |______
  ______(_)(_)___|________________|___jro


endendendendendendendendendendendendendend
endendendendendendendendendendendendendend
'''
]

import os

rare_old_items = [
    "Antique pocket watch from 1800s",
    "Vintage typewriter from early 1900s",
    "Ancient Roman coin",
    "Rare first edition classic novel",
    "Victorian era jewelry",
    "Original 19th-century oil painting",
    "Ancient Egyptian artifact",
    "Medieval knight’s helmet",
    "Early 20th-century phonograph",
    "Rare collectible stamp from 19th century",
    "Antique globe from the Age of Exploration",
    "Old handwritten manuscript",
    "Vintage movie poster from 1920s",
    "Rare fossilized dinosaur bone",
    "Ancient Chinese porcelain vase",
    "Early mechanical calculator",
    "Vintage camera from 1930s",
    "Old pirate map reproduction",
    "Antique chess set made from ivory",
    "Rare jazz vinyl record from 1940s"
]
print(random.choice(logo))

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')




