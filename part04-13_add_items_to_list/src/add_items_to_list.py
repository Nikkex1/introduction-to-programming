# Write your solution here
my_list = []
times = int(input("How many items:"))
x = 1

while times > 0:
    item = int(input(f"Item {x}:"))
    my_list.append(item)
    times -= 1
    x += 1
print(my_list)