# Write your solution here
limit = int(input("Limit:"))
number = 1
nsum = 0
stringsum = ""

while nsum < limit:
    nsum += number
    if nsum < limit:
        stringsum += f"{number} + "
    number += 1
    
print(f"The consecutive sum: {stringsum}{number - 1} = {nsum}")