# Write your solution here
word = input("Please type in a string: ")
index = 0

while index > len(word) * -1:
    index -= 1
    print(word[index])
    