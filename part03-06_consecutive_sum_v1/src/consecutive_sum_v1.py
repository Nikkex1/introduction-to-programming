# Write your solution here
limit = int(input("Limit:"))
number = 1
nsum = 0

while nsum < limit:
    nsum += number
    number += 1

print(nsum)