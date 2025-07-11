# Write your solution here
word = input("Please type in a word:")
char = input("Please type in a character:")

if char in word:
    index = word.find(char)
    if len(word[index:index+3]) >= 3:
        print(word[index:index+3])