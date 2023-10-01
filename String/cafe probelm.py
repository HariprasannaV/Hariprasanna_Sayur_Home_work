import re

menu_card = ["tea", "vada", "coffee", "biscuit"]
price = [20, 5, 20, 10]
cost_price = [15, 3, 15, 7]  # Cost prices for each item
item_quantity = [100, 150, 100, 50]
pattern = r'(\d*)\s*(' + '|'.join(menu_card) + ')'

initial_quantity = item_quantity.copy()

while True:
    order = input("What do you need (Enter 'q' to quit): ").lower()

    if order == 'q':
        break

    # Use regular expression to extract numbers and items
    numbers = re.findall(r'\d+\.\d+|\d+', order)
    items = re.findall(pattern, order, re.IGNORECASE)
    print(numbers)
    print(items)

    total = 0
    for i in range(len(items)):
        if items[i] in menu_card:
            index = menu_card.index(items[i])
            num = int(numbers[i])

            if item_quantity[index] < num:
                print(f'Sorry, we have only {item_quantity[index]} {menu_card[index]} left.')
            else:
                item_quantity[index] -= num
                cost = price[index] * num
                total += cost
                print(f'Added {num} {menu_card[index]} to your order. Cost: {cost} INR')

    print(f'Your total bill: {total} INR')

    if all(quantity == 0 for quantity in item_quantity):
        print("All items are out of stock.")
        profit = sum(
            (price[i] - cost_price[i]) * (initial_quantity[i] - item_quantity[i]) for i in range(len(menu_card)))
        print(f"Total Profit: {profit} INR")
        break

#
# import re
#
# # List of fruits the vendor has
# menu_card = ["tea", "vada", "coffee", "biscuit"]
# price = [20, 5, 20, 10]
# profit_price = [5, 2, 5, 3]
# item_quantity = [100, 150, 100, 50]
# remaining_quantity = []
#
# initial_quantity = item_quantity.copy()
#
# # Regular expression pattern to match fruit and quantity
# pattern = r'(\d*)\s*(' + '|'.join(menu_card) + ')'
#
# while True:
#     # Simulate a customer request
#     request = input("what do you need: ")
#     match = re.findall(pattern, request, re.IGNORECASE)
#     # print(match)  #
#
#     total = 0
#
#     for i in range(len(match)):
#         print(i)
#         if match:
#             item = match[i][1]
#             quantity = int(match[i][0])
#             position_of_item = menu_card.index(item)
#             price_of_item = int(price[position_of_item])
#             cost = price_of_item * quantity
#             print(position_of_item)
#             print(price_of_item)
#             if match[i] in menu_card:
#                 index = menu_card.index(match[i])
#                 num = int(quantity)
#
#                 if item_quantity[index] < num:
#                     print(f'Sorry, we have only {item_quantity[index]} {menu_card[index]} left.')
#                 else:
#                     if quantity:
#                         print(f"You want {quantity} X {item} = {cost}.")
#                     else:
#                         quantity = input(f"How many {item} do you want? ")
#                         print(f"You want {quantity} X {item} = {cost}.")
#             total += cost
#
#         else:
#             print("Sorry, I didn't understand that. Please specify the fruit and quantity.")
#     print(f'Your total bill: Rs.{total} ')
#
#     if all(quantity == 0 for quantity in item_quantity):
#         print("All items are out of stock.")
#         profit = sum(
#             (price[i] - price[i]) * (initial_quantity[i] - item_quantity[i]) for i in range(len(menu_card)))
#         print(f"Total Profit: {profit} INR")
#         break
