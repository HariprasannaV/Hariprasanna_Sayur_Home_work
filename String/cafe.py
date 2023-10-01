import re

menu_card = ["tea", "vada", "coffee", "biscuit"]
price = [20, 5, 20, 10]
profit_price = [5, 2, 5, 3]
item_quantity = [100, 150, 100, 50]
remaining_quantity = []

while True:
    order = input("What do you need:")

    # Use regular expression to extract numbers and items
    numbers = re.findall(r'\d+\.\d+|\d+', order)
    items = re.findall(r'\b(coffees?|teas?|vada|biscuits?)\b', order.lower())
    print(numbers)
    print(items)

    total = 0
    for i in range(len(items)):
        index = menu_card.index(items[i])
        num = int(numbers[i])
        print(index)
        item_quantity[index] -= num
        print(item_quantity)
        if item_quantity[index] == 0 or item_quantity[index] < num:
            item_quantity[index] = 0
            print(f'We have only {item_quantity[index]} ')
            print("This Item is not available")
            continue

        else:
            cost = price[i] * num
            print(f'The price of {menu_card[index]} is {cost}')
            total += cost

    print(f'total {total}')
