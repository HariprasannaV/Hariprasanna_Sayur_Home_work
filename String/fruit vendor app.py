"""
Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking.
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp
You can limit the quantity to single digit number.
"""

import re

# List of fruits the vendor has
fruits = ['apple', 'orange', 'banana']

# Regular expression pattern to match fruit and quantity
pattern = r'(\d*)\s*(' + '|'.join(fruits) + ')'


# Simulate a customer request
request = input("what do you need: ")
match = re.search(pattern, request, re.IGNORECASE)
print( match.group(2))
print(match.group(0))

if match:
    fruit = match.group(2).lower()
    quantity = match.group(1)

    if quantity:
        print(f"You want {quantity} {fruit}(s).")
    else:
        quantity = input(f"How many {fruit}(s) do you want? ")
        print(f"You want {quantity} {fruit}(s).")
else:
    print("Sorry, I didn't understand that. Please specify the fruit and quantity.")

"""
Output:

Your Request here>> i need 3 apple
You want 3 apple(s).

"""