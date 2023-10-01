import re

menu_card = ["tea", "vadai", "coffee", "biscuit"]
price = [20, 10, 20, 10]
item_quantity = [100, 150, 100, 100]
initial_quantity =[100, 150, 100, 100]
reviews=[]
expenses=0
total=0
cost_price=[10,5,10,5]
for cost in range (len(item_quantity)):
    expenses += item_quantity[cost]*cost_price[cost]
while True:
    if item_quantity != [0,0,0,0]:
        choice=input("did the customers visit the shop(yes/no)?")
        if choice.lower() == "yes":
            print(f"{'*'*10}MENU{'*'*10}")
            for no,item in enumerate(menu_card) :
                print(f"  {no+1}) {item}\t-{price[no]}rs ")
            order = input("What you need:")
            # Use regular expression to extract numbers
            numbers = re.findall(r'(\d+)\s+(?:coffee|tea|biscuit|vadai)', order)
            items = re.findall(r'\b(coffees?|teas?|vadais?|biscuits?)\b', order)
            bill = 0
            print(f"{'*'*10}bill{'*'*10}")
            for i in range(len(items)):
                index = menu_card.index(items[i])
                num = int(numbers[i])
                if item_quantity[index] == 0 or item_quantity[index] < num:
                    print("This Item is not available")
                else:
                    item_quantity[index] -= num
                    cost = price[index] * num
                    print(f' {menu_card[index]} X {num} \t : {cost}rs')
                    bill += cost
            total+=bill
            print("*"*24)
            print(f'total amount: {bill}')
            reviews.append(input("enter your review:"))
            print("thank you for the review :)")
        elif choice.lower()=="no":
            print("we are closed")
            print(f"expenses :\t{expenses}")
            print("remaining items")
            for Num,Items in enumerate(menu_card):
              print(f" {Items} initially in the store : {initial_quantity[Num]}  remaining:{item_quantity[Num]}")
            print(f"total money earned:{total}")
            for customer,review in enumerate(reviews):
                print(f"review from customer-{customer+1} is {review}")
            if total > expenses:
                print(f"profit:{total-expenses}Rs")
            elif total < expenses:
                print(f"loss:{total-expenses}Rs")
            else:
                print(f"neither profit nor loss:{total-expenses}Rs")
        else:
            print("invalid input")
    else:
        print("we are closed")
        print(f"expenses :\t{expenses}")
        print("remaining items")
        for Num,Items in enumerate(menu_card):
            print(f" {Items} initially in the store : {initial_quantity[Num]}  remaining:{item_quantity[Num]}")
        print(f"total money earned:{total}")
        for customer,review in enumerate(reviews):
            print(f"review from customer-{customer+1} is {review}")
        if total > expenses:
            print(f"profit:{total-expenses}Rs")
        elif total < expenses:
            print(f"loss:{total-expenses}Rs")
        else:
            print(f"neither profit nor loss:{total-expenses}Rs")
        break

