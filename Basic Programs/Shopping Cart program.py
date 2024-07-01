'''
    SHOPPING CART PROGRAM
    DESCRIPTION:
    => This program will ask the user for the food stuffs he is buying and their corresponding prices, 
       then print the total price, in a good manner.
    => Now the user must make sure he enters a food item or if he wants to quit e must press the q letter to quit.

'''

foodStuff = []
prices = []
total = 0
while True:
    food = input("Enter a food stuff: (press q for quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price for the food: XAF "))
        foodStuff.append(food)
        prices.append(price)

print("------- SHOPPING CART ---------")

for food in foodStuff:
    print(food, end = "\t")
print()

for price in prices:
    total += price
    print(price, end ="\t")

print(f"\nTotal: XAF{total}")

