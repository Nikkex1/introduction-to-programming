# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year:"))
date = datetime(year, month, day)

difference = (datetime(1999,12,31) - date).days

if difference > 0:
    print(f"You were {difference} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")