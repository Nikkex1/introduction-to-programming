# Write your solution here
limit = int(input("Please type in a number:"))
i = 1
sec = 1

while i <= limit:
    while sec <= limit:
        print(f"{i} x {sec} = {i*sec}")
        sec += 1
    i += 1
    sec = 1