# Write your solution here
times_eaten = int(input("How many times a week do you eat at the student cafetaria?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week? \n"))
print("Average food expenditure:")
print(f"Daily: {(times_eaten * lunch_price + groceries) / 7} euros")
print(f"Weekly: {times_eaten * lunch_price + groceries} euros")