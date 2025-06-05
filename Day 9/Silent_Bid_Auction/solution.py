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
''',

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
bid_item = random.choice(rare_old_items)
print(f"This is a silent bidding auction for {bid_item}")

continuing = False
bids = {}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bid_finder(bids):
    highest_bid = 0
    highest_bidder = ''
    for key, value in bids.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    print(f"The {bid_item} is sold out to {highest_bidder} who made the highest bid of ${highest_bid}. Congrats 🎉!")

while not continuing:
    bidder_name = input("Enter you name: ")
    bid_amount = int(input("Enter the bid amount in '$': $"))
    bids[bidder_name] = bid_amount
    wanna_continue = input("Is there an another bidder? 'yes' or 'no': ")
    if wanna_continue == 'yes':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
              "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        clear_console()
    elif wanna_continue == 'no':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
              "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"Bidding is over!")
        highest_bid_finder(bids)
        continuing = True
    else:
        print("Please enter something valid!")












