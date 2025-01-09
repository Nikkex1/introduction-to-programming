# Write your solution here
story = ""
new = ""
while True:
    word = input("Please type in a word")
    if word == "end":
        print(story)
        break
    elif new == word:
        print(story)
        break
    new = word
    story += word + " "
    