"""
########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = #FillinMissingCode
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split(): #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
         #FillinMissingCode - check if the char is vowel or not



    word = #FillinMissingCode
    print( #FillinMissingCode)

"""

inputSentence = str(input("Enter the sentence: "))
pigLatinKey = 'ay'
vowels = ['a', 'e', 'i', 'o', 'u']

for word in inputSentence.split():  # Splitting the sentence into words

    first_vowel_index = 0

    # Find the index of the first vowel in the word
    for index, char in enumerate(word):
        if char.lower() in vowels:
            first_vowel_index = index
            break

    if first_vowel_index > 0:
        word = word[first_vowel_index:] + word[:first_vowel_index] + pigLatinKey   # If there is a vowel, move the consonants to the end and add 'ay'
    else:
        word = word + pigLatinKey         # If the word starts with a vowel, simply add 'ay' to the end

    print(word)

"""
Output:
Enter the sentence: I am python
Iay
amay
onpythay

"""