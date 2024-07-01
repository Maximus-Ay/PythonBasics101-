'''
    CONCESSION STAND PROGRAM
    => This program is meant to deepen our understanding of dictionaries
    => We will use a dictionary to be able to print a menu.
    => And the user will choose an item and we will calculate the price


'''

menu = {"Achu": 3.40,
        "Sandwich": 4.99,
        "Ice Cream": 5.8,
        "Nacho": 3.4,
        "Bretzel": 2.7
        }

cart = []
total = 0
print("--------- MENU --------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("------------------------------------")


while True:
    food = input("Enter your food choice (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu[food]

print(f"Your list is {cart} and total price is: ${total}")

