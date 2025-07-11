# Write your solution here
limit = int(input("Please type in a number:"))
i = 2

while i <= limit:
    print(i)
    print(i - 1)
    i += 2

if limit % 2 != 0:
    print(limit)