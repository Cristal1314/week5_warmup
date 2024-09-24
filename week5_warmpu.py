# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 
text = "abracadabra"
# a. Retrieve the 5th character.
substring = text.find[0 :5]
print(substring)
# b. Retrieve the second to last character.
substring = text.find[-2]
print(substring)
# c. Find the first occurrence of the letter 'c'.
substring = text.find("c")
print(substring)
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
text2 = "hij"
substring = text2.find("hij")
print(substring)
# b. Extract every second letter starting from 'a' to 'm'.
substring = text2.find("m")
print(substring)
substring = text2.find[0:14:1]
# c. Reverse the entire string using slicing.

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text = "Ask not what your country can do for you - ask what can you do for your country. - John F. Kennedy"
print(text.find("John"))
print(text[83:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
text = "Python is fun. Fun is good. Good is subjective"
substring = text.find("subjective")
print(substring)
# b. Extract every third word.
substring = text[0:-1:3]

# c. Reverse the positions of the words, but keep the characters in each word in the same order.


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
result="MAY THE FORCE BE WITH YOU ".lower
print (result)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
word_list = ["Make", "haste", "slowly"]
joined_list = "".join(word_list)
print(joined_list)
# b. Now, split the string at every occurrence of the letter 'a'.# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
text="Life is what happens when you are busy making other plans "
result1= text.replace("busy","distracted").replace("plans","mistakes")
print(result1) 
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
cat="Iteration"
print(cat* 7)
# Word Search:
# Check if the word "moonlight" appears in the quote: 
text = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote="With freedom,books,flowers,and the moon, who could not be happy?-Oscar Wilde"
if "moonlight"in quote: print ("Moonlight is in the quote")
text.find("moonlight")
print(text.find)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: 
text = "Supercalifragilisticexpialidocious"
text.find("Supercalifragilisticexpialidocious")
print(text.find)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
my_string="Supercalifragilisticexpialidocious" 
num_characters=len(my_string)
count = my_string.find("i")
print (num_characters)
total=count("i") in my_string 
print (total)