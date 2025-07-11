# Write your solution here
word = input("Please type in a string:")
char = input("Please type in a substring:")
index = word.find(char)
second = word.find(char,index+len(char))

if second != -1:
    print(f"The second occurrence of the substring is at index {second}.")
else:
    print("The substring does not occur twice in the string.")