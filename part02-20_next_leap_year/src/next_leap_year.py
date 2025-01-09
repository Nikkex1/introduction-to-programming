# Write your solution here
year = int(input("Year:"))
nextyear = year + 1

while True:
    if nextyear % 4 == 0 and nextyear % 100 != 0 or nextyear % 400 == 0:
        break
    nextyear += 1
print(f"The next leap year after {year} is {nextyear}")