"""
########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = #FillinMissingCode
pigLatinKey = 'ay'
for word in inputSentence.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
     #FillinMissingCode - check if the word has more than one char

    word = word[1:] + firstChar + pigLatinKey
    print( #FillinMissingCode)
"""

inputSentence = "i am python"  # this is input sentence
pigLatinKey = 'ay'

for word in inputSentence.split():                                               # Splitting the sentence into words
    firstChar = word[0]                                       # Taking the first character of the word

    if len(word) > 1:                                                 # Checking if the word has more than one character
        word = word[1:] + firstChar + pigLatinKey
    else:
        word = firstChar + pigLatinKey                                  # Handling single-character words differently

    print(word, end=' ')

"""
Output:
iay maay ythonpay 
"""