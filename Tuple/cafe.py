import re

# List of fruits the vendor has
menu_card = [("tea", 20), ("vada", 5), ("coffee", 20), ("biscuit", 10)]
item_quantity = [100, 150, 100, 50]

# Regular expression pattern to match fruit and quantity
pattern = r'(\d*)\s*(' + '|'.join(item[0] for item in menu_card) + ')'

while True:
    # Simulate a customer request
    request = input("What do you need: ")
    match = re.findall(pattern, request, re.IGNORECASE)
    print(match)

    total = 0

    for i in range(len(match)):
        if match:
            item = match[i][1]
            quantity = int(match[i][0])
            menu_item = next((x for x in menu_card if x[0] == item), None)

            if menu_item is not None:
                price_of_item = menu_item[1]

                if item_quantity[i] >= quantity:
                    item_quantity[i] -= quantity
                else:
                    if item_quantity[i] > 0:
                        quantity = item_quantity[i]
                        print(f'There is only {quantity} of {item}')
                        item_quantity[i] = 0
                    else:
                        quantity = 0
                        print("The item is not available")

                cost = price_of_item * quantity

                if quantity:
                    print(f"You want {quantity} X {item} = {cost}.")
                else:
                    quantity = input(f"How many {item} do you want? ")
                    cost = price_of_item * int(quantity)
                    print(f"You want {quantity} X {item} = {cost}.")
                total += cost

        else:
            print("Sorry, I didn't understand that. Please specify an item.")
    print(f'Your total bill: Rs.{total} ')
