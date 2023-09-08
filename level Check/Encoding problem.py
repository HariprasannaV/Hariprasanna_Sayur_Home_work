
# # Input message and pattern
#
# sentence = str(input("Enter the Sentence: \n"))
# pattern = str(input("Enter the star pattern: \n"))
#
# # Initialize an empty string for the encoded message
# encoded_message = ""
# message_index = 0
#
# # Iterate through the pattern
# for char in pattern:
#     if char == ' ':
#         encoded_message += ' '  # If the pattern has a space, add a space to the encoded message.
#     else:
#         # If the pattern has an asterisk, add the corresponding character from the message.
#         encoded_message += message[message_index]
#         message_index += 1
#
# # Print the encoded message
# print(encoded_message)
# Input message and pattern
message = "I Love India"
pattern = "*** **** ** **********     *****"

# Initialize an empty string for the encoded message
encoded_message = ""
message_index = 0

# Iterate through the pattern
for char in pattern:
    if char == ' ':
        encoded_message += ' '  # If the pattern has a space, add a space to the encoded message.
    else:
        # If the pattern has an asterisk, add the corresponding character from the message.
        encoded_message += message[message_index]
        message_index += 1

# Print the encoded message
print(encoded_message)
