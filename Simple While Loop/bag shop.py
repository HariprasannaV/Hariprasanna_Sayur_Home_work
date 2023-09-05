"""
########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold.
#Display total sales and total number of bags sold

#initialize variables
redBags, greenBags = 100, 200
totalSales , totalBagsSold = 0

while (totalSales < 10000 or totalBagsSold < 10) :
    #Ask customer for input
    #FillinMissingCode

    #calculate total cost for the bags
     #FillinMissingCode
    totalSales +=  #FillinMissingCode
    #increment no of bags sold
    totalBagsSold +=  #FillinMissingCode

print ( #FillinMissingCode)
"""
# Initialize variables
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0,0

while totalSales < 10000 and totalBagsSold < 10:
    # Ask customer for input
    bag_color = input("Enter the bag color (red or white): ").lower()
    quantity = int(input("Enter the quantity of bags: "))

    if bag_color == "red" and redBags >= quantity:
        cost = 1000 * quantity
        redBags -= quantity
    elif bag_color == "white" and whiteBags >= quantity:
        cost = 1500 * quantity
        whiteBags -= quantity
    else:
        print("Sorry, we don't have enough bags of the selected color.")
        continue

    # Calculate total cost for the bags
    totalSales += cost
    # Increment the number of bags sold
    totalBagsSold += quantity

print("Total sales:", totalSales)
print("Total number of bags sold:", totalBagsSold)
