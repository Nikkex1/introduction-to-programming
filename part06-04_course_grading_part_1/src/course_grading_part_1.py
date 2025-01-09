# write your solution here
if True: #if True: always executed; if False: never executed
    student_info = input("Student information:")
    exercise_data = input("Exercised completed:")
else: #hard coded input for testing
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

dictionary = {}
with open(student_info) as student_file:
    for line in student_file:
        #line = line.replace("\n", "") #strip() is more efficient
        line = line.strip() #strip removes everything unnecessary
        parts = line.split(";")
        if parts[0] == "id":
            continue
        dictionary[parts[0]] = [f"{parts[1]} {parts[2]}"]


with open(exercise_data) as exercise_file:
    for line in exercise_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for number in parts[1:]:
            dictionary[parts[0]].append(int(number))

help_sum = 0
for key, value in dictionary.items():
    for item in value[1:]:
        help_sum += item
    print(f"{value[0]} {help_sum}")
    help_sum = 0