"""
Write a program for calculating the profit for railways.
For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

Get the price and no of tickets sold for each class and calculate the total profit.
Identity what calculation in the above problem can be written as a function
and what the input and output should be.
"""


def calculate_profit(price, num_tickets, fixed_amount, percentage):
    return percentage * price * num_tickets + fixed_amount * num_tickets


# Get input from the user
first_class_price = float(input("Enter the price of a first class ticket: "))
first_class_tickets = int(input("Enter the number of first class tickets sold: "))

second_class_price = float(input("Enter the price of a second class ticket: "))
second_class_tickets = int(input("Enter the number of second class tickets sold: "))

third_class_price = float(input("Enter the price of a third class ticket: "))
third_class_tickets = int(input("Enter the number of third class tickets sold: "))

# Example usage:
first_class_profit = calculate_profit(first_class_price, first_class_tickets, 100,0.25 )
second_class_profit = calculate_profit(second_class_price, second_class_tickets, 70, 0.15)
third_class_profit = calculate_profit(third_class_price, third_class_tickets, 0,0.05)

# Calculate and display the total profit
total_profit = first_class_profit + second_class_profit + third_class_profit
print(f"The total profit for the railways is: Rs. {total_profit}")
