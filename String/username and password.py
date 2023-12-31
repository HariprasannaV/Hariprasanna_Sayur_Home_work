"""
2. Check if the username and password is correct.
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123
"""

# Input username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

numbers = [0,1,2,3,4,5,6,7,8,9]

# Check if the username and password are correct
if '@' in username and (username.endswith('.com') or username.endswith('.edu') or username.endswith('.tech') or username.endswith('.org')):
    # Extract the first, third, and last 3 letters of the username
    modified_username = username.split('@')
    word = modified_username[0]
    first_letter = word[0]
    third_letter = word[2]
    last_three = word[-3:]

    # Extract the company name from the username
    company_name = username.split('@')[1].split('.')[0][:3]
    # print(company_name)

    # Construct the expected password
    expected_password = first_letter + third_letter + last_three + company_name + "123"
    # print(expected_password)

    # Check if the entered password matches the expected password
    if password == expected_password:
        print("Username and password are correct.")
    else:
        print("Username and/or password are incorrect.")
else:
    print("Invalid username format.")

"""
output:
Enter your username: myname@sayur.com
Enter your password: mnamesay123

Username and password are correct.
"""

"""
# Get user input as a string
user_input = input("Enter a number: ")

# Check if the input is a three-digit number
if user_input.isdigit() and len(user_input) == 3:
    print(f"The input {user_input} is a three-digit number.")
else:
    print(f"The input {user_input} is not a three-digit number.")
"""