# Write your solution here
first = input("1st letter:")
second = input("2nd letter:")
third = input("3rd letter:")
if first > second and first > third:
    if second > third:
        middle = second
    else:
        middle = third
elif second > first and second > third:
    if first > third:
        middle = first
    else:
        middle = third
elif third > first and third > second:
    if first > second:
        middle = first
    else:
        middle = second
print(f"The letter in the middle is {middle}")