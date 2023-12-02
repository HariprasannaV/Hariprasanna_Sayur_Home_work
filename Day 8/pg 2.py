"""
Write a program that calculates the profit generated by a movie theatre for different ticket classes.

For VIP tickets, the profit is 30% of the ticket price + Rs120 for every ticket sold.
For General tickets, the profit is 20% of the ticket price + Rs80 for every ticket sold.
For Matinee show tickets, the profit is a flat 15% of the ticket price.
Input: Ticket price and number of tickets sold for each ticket class.
Output: Calculate and print the total revenue generated by the theatre in a day.
"""


def calculate_profit(price, num_tickets, percentage, fixed_amount=0):
    return percentage * price * num_tickets + fixed_amount * num_tickets


# Get input from the user
vip_price = float(input("Enter the price of a VIP ticket: "))
vip_tickets = int(input("Enter the number of VIP tickets sold: "))

general_price = float(input("Enter the price of a General ticket: "))
general_tickets = int(input("Enter the number of General tickets sold: "))

matinee_price = float(input("Enter the price of a Matinee show ticket: "))
matinee_tickets = int(input("Enter the number of Matinee show tickets sold: "))

# Calculate profits for each ticket class
vip_profit = calculate_profit(vip_price, vip_tickets, 0.3, 120)
general_profit = calculate_profit(general_price, general_tickets, 0.2, 80)
matinee_profit = calculate_profit(matinee_price, matinee_tickets, 0.15)

# Calculate and display the total revenue
total_revenue = vip_profit + general_profit + matinee_profit
print(f"The total revenue generated by the theatre in a day is: Rs. {total_revenue}/-")