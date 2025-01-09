# Write your solution here
word = input("Word:")
print("*"*30)
if len(word) % 2 == 0:
    print("*" + " " * int(14 - len(word) / 2) + word + " " * int(14 - len(word) / 2) + "*")
else:
    print("*" + " " * int(14 - len(word) / 2) + word + " " * int(15 - len(word) / 2) + "*")
print("*"*30)