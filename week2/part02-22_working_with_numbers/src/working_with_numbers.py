# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
nsum = 0
poscount = 0
negcount = 0

while True:
    number = int(input("Number:"))
    if number == 0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {nsum}")
        print(f"The mean of the numbers is {nsum / count}")
        print(f"Positive numbers {poscount}")
        print(f"Negative numbers {negcount}")
        break
    if number > 0:
        poscount += 1
    if number < 0:
        negcount += 1
    count += 1
    nsum += number