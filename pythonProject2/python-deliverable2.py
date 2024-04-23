# Begin fruit program

#create variable for user name
user_name = input("May I please have your name?")

#welcome message
print(f"Hello {user_name}, welcome to the fruit market. Let's shop.")

# store the available fruits and their respectice prices
fruit_prices = { "apple": 2,"grape": 1, "orange": 3}

#Create variables for user fruit order and running total cost
fruit_order_list = []
total_cost = 0

while True:
    print("Here is the list of fruits available and their prices:")
    for fruit, price in fruit_prices.items():
     print(f"{fruit.capitalize()}: ${price}")

#add space
    print()

# Ask user which fruit they'd like to purchase
    chosen_fruit = input("Please type the name of fruit you'd like to buy:").lower()
    if chosen_fruit == 'done':
         break

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

#Calculate order cost and total cost
    fruit_cost = fruit_prices[chosen_fruit] * quantity
    total_cost += fruit_cost

    fruit_order_list.append((chosen_fruit, quantity, fruit_cost))

#Ask user if they would like more fruit
    buy_more_fruit = input("Would you want to buy another piece of fruit? (y/n): ").lower()
    if buy_more_fruit != 'y':
        break

subtotal = total_cost

# Calculate tax
tax_rate = 0.05
tax_amount = (subtotal * tax_rate) + subtotal

# Overall total

# User order with list of fruit types & prices
print(f"Receipt for {user_name}:")
for order in fruit_order_list:
    fruit_name = order[0]
    quantity = order[1]
    fruit_price = order[2] / quantity # Calculate price per fruit
    print(f"{quantity} {fruit_name}s - ${fruit_price: .2f} each")

# Subtotal display
print(f"\nSubtotal: ${subtotal: .2f}")

# Tax amount display
print(f"Tax (5%): ${tax_rate: .2f}")

# Overall total
print(f"Total (including tax): ${tax_amount: .2f}")

# Final thank you note
print("Thank you for shopping at the fruit market!")

