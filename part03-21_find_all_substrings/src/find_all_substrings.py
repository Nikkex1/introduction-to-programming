# Write your solution here
word = input("Please type in a word:")
char = input("Please type in a character:")

if char in word:
    index = word.find(char)
    while len(word[index:index+3]) >= 3:
        if char == word[index:index+1]:
            print(word[index:index+3])
        index += 1