# Write your solution here
students = int(input("How many student on the course?"))
group_size = int(input("Desired group size?"))
print(f"Number of groups formed: {(students // group_size) + (students % group_size > 0)}")