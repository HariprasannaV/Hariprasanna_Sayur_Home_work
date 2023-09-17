"""
String manipulation exercises. Use builtin functions as needed.

1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.
"""

# Iterate for a maximum of 3 times
for times in range(3):

    inputPassword = str(input("Enter the New Password: "))
    print("print at least 3 alphabets , 2 numbers , 2 special characters")

# Initialize counts for different character types
    capital_count = 0
    small_count = 0
    digit_count = 0
    special_count = 0

# Iterate through each character in the inputPassword to count character types
    for char in inputPassword:
        if char.islower():
            small_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    # Check if the password length is less than 8 characters
    if len(inputPassword) < 8:
        print(f'Your Password must contain 8 Characters ')
        print('please try again')
        continue  # Continue to the next iteration

    # Check for weak passwords with exactly one character type
    elif small_count == 1 or digit_count == 1 or special_count <= 1:
        print('weak')
        print('please try again')
        continue  # Continue to the next iteration

    # Check for moderately strong passwords
    elif 3 >= small_count >= 1 or 2 >= digit_count >= 1 or special_count == 2:
        print('ok')
        break  # Exit the loop as it's strong enough

    # Check for very strong passwords
    elif (small_count >= 3 or digit_count >= 2 or special_count > 2) and len(inputPassword) >= 16:
        print('Very strong')
        break  # Exit the loop as it's very strong

    # Check for strong passwords
    elif small_count >= 3 or digit_count >= 2 or special_count >2:
        print('strong')
        break  # Exit the loop as it's strong enough

    # If none of the conditions match, prompt the user to try again
    else:
        print("Please try another time")
        print(f'you have only {2 - times} chances remaining')  # Calculate and display remaining chances
