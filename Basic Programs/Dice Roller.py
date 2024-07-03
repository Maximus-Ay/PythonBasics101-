'''
    DICE ROLLER GAME
    => This will improve knowledge on random numbers.
    => To get a good representation of the dies we are going to use some ASCII arts.
    => We ill use unicode to get the characters to draw our die
'''

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# ┌─────────┐
# │         │
# │    ●    │
# │         │
# └─────────┘
import random
dice_art = {
    1: (
        "┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"
        ),
    2: (
        "┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"
    ),
    3: (
        "┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"
    ),
    4: (
        "┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"
    ),
    5: (
        "┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"
    ),
    6:(
        "┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘"
    )
}

# So our objective is to ask the user the number of times, he will want to roll the dice and calculate the total

dice = []
total = 0
number_of_rolls = int(input("Enter the number of rolls: "))

# Let's print the values obtained

for roll in range(number_of_rolls):
    dice.append(random.randint(1,6))

# let's calculate the total:
for roll in dice:
    total += roll
# Let us print our dice art now
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

print(f"Total: {total}")

