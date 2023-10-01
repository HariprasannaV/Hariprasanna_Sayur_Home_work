import re

# List of fruits the vendor has
menu_card = ["tea", "vada", "coffee", "biscuit"]
price = [20, 5, 20, 10]
profit_price = [5, 2, 5, 3]
item_quantity = [100, 150, 100, 50]
remaining_quantity = []

# initial_quantity = item_quantity.copy()

# Regular expression pattern to match fruit and quantity
pattern = r'(\d*)\s*(' + '|'.join(menu_card) + ')'

while True:
    # Simulate a customer request
    request = input("what do you need: ")
    match = re.findall(pattern, request, re.IGNORECASE)
    print(match)

    total = 0

    for i in range(len(match)):
        # print(i)

        if match:
            item = match[i][1]
            print("27 item",item)
            quantity = int(match[i][0]) # 5
            print('29 quantity',quantity)
            position_of_item = menu_card.index(item)
            print('31 position_of_item',position_of_item)
            price_of_item = int(price[position_of_item])
            print('33 price_of_item',price_of_item)

            # print(position_of_item)
            # print(price_of_item)
            if item_quantity[position_of_item] >= quantity: # 100 >=3
                item_quantity[position_of_item] -= quantity

            else:
                if item_quantity[position_of_item] > 0:
                    quantity = item_quantity[position_of_item]  # quantiy = 1
                    print(f'There is only {quantity} of {item}')
                    item_quantity[position_of_item] = 0
                else:
                    quantity = 0
                    print("The item is not available")

            cost = price_of_item * quantity


            if quantity:
                print(f"You want {quantity} X {item} = {cost}.")
            else:
                quantity = input(f"How many {item} do you want? ")
                print(f"You want {quantity} X {item} = {cost}.")
            total += cost

        else:
            print("Sorry, I didn't understand that. Please specify item.")
    print(f'Your total bill: Rs.{total} ')

