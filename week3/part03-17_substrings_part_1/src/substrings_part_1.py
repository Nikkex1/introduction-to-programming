# Write your solution here
string = input("Please type in a string:")
number = 1
while number <= len(string):
    print(string[0:number])
    number += 1