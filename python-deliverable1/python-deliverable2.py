# Begin fruit program

#create variable for user name
user_name = input("May I please have your name?")

#welcome message
print(f"Hello {user_name}, welcome to the fruit market. Let's shop.")

#add space within the program
print()

# store the available fruits and their respectice prices
fruit_prices = { "Apple": 2,"Grape": 1, "Orange": 3}

print("Here is the list of fruits available and their prices:")
for fruit, price in fruit_prices.items():
    print(f"{fruit.capitalize()}: ${price}")

#add space
print()

# Ask user which fruit they'd like to purchase
chosen_fruit = input("Please type the name of fruit you'd like to buy").lower()

# Check if the chosen fruit is valid
if chosen_fruit not in fruit_prices:
    print("Sorry, please enter fruit from the list provided")
    continue

# Ask user for quantity of fruit
while True:
    try:
        quantity = int(input(f"How many {chosen_fruit}s do you want to buy?"))
        if quantity < 0:
            print("Please enter a non-negative quantity.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer")