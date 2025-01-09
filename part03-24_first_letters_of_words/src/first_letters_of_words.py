# Write your solution here
word = input("Please type in a sentence:")
print(word[0:1])
empty = word.find(" ")

while empty <= len(word):
    if word[empty:empty + 1] == " ":
        print(word[empty + 1:empty + 2])
        empty += 1
    else:
        empty += 1