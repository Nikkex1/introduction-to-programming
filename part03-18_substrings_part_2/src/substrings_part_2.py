# Write your solution here
string = input("Please type in a string:")
number = len(string)
while number > 0:
    number -= 1
    print(string[number:])
    