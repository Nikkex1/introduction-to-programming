# Write your solution here
from datetime import datetime, timedelta

time_dict = {}

if True:
    filename = input("Filename:")
    start_date = input("Starting date:")
    parsed_date = datetime.strptime(start_date, "%d.%m.%Y")
    length = int(input("How many days:"))
    print("Please type in screen time in minutes on each day (TV computer mobile)")
    for i in range(length):
        date = parsed_date + timedelta(days=i)
        date = date.strftime("%d.%m.%Y")
        screen_time = input(f"Screen time {date}:")
        time_dict[date] = screen_time

else: #for testing
    filename = "file.txt"
    start_date = "1.6.2020"
    parsed_date = datetime.strptime(start_date, "%d.%m.%Y")
    length = 5
    print("Please type in screen time in minutes on each day (TV computer mobile)")
    for i in range(length):
        date = parsed_date + timedelta(days=i)
        date = date.strftime("%d.%m.%Y")
        screen_time = "120 60 30"
        time_dict[date] = screen_time

with open(filename, "w") as my_file:
    pass

minutes = []
for key in time_dict:
    value = time_dict[key].split(" ")
    for item in value:
        minutes.append(int(item))

total = sum(minutes)
average = total / length

with open(filename, "a") as my_file:
    my_file.write(f"Time period: {parsed_date.strftime("%d.%m.%Y")}-{date}\n")
    my_file.write(f"Total minutes: {total}\n")
    my_file.write(f"Average minutes: {average}\n")
    for key, value in time_dict.items():
        value = value.split()
        my_file.write(f"{key}: {value[0]}/{value[1]}/{value[2]}\n")