# Define the menu items and their prices
menu_card = ["tea", "vadai", "coffee", "biscuit"]
price = ["15", "5", "12", "10"]

# Display the menu to the user
print("Here are the menu items and their prices:")
for i in range(len(menu_card)):
    print(f'{i + 1}. {menu_card[i]} = {price[i]}')

# Initialize empty lists to store orders and quantities
myOrders_array = []
count_array = []

# Ask the user for their order in a loop
while True:
    user_input = input("Enter your order (or 'enough' to close the menu): ")

    if user_input.lower() == 'enough':
        break  # Exit the loop if the user enters 'enough'

    if user_input not in menu_card:
        print("You have entered a wrong item or it's not on the menu")
    else:
        # Append the user's order to the array
        myOrders_array.append(user_input)

# Print the user's order
print("Your order:")
for index, order in enumerate(myOrders_array):
    user_input_2 = input(f'How many {myOrders_array[index]} do you want: ')
    count_array.append(int(user_input_2))

# Print the items and quantities in the order
print("You ordered:")
for i in range(len(myOrders_array)):
    print(f'{myOrders_array[i]} x{count_array[i]}')

total_price_amount = 0
# Calculate the total bill
# Loop through the items in the user's order
for i in range(len(myOrders_array)):
    # Get the current item and its quantity from the lists
    item = myOrders_array[i]
    quantity = count_array[i]

    # Find the index of the item in the menu to look up its price
    item_index = menu_card.index(item)

    # Get the price of the item from the price list and convert it to an integer
    item_price = int(price[item_index])

    # Calculate the cost of the current item by multiplying its price by the quantity
    item_cost = item_price * quantity

    # Add the cost of the current item to the total bill amount
    total_price_amount += item_cost

# Print the total bill amount
print("Total bill amount:", total_price_amount)
