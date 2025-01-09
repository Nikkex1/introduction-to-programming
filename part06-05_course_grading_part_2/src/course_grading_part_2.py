# write your solution here
if True: #if True: always executed; if False: never executed
    student_info = input("Student information:")
    exercise_data = input("Exercised completed:")
    exam_data = input("Exam points:")
else: #hard coded input for testing
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

name_dictionary = {}
with open(student_info) as student_file:
    for line in student_file:
        #line = line.replace("\n", "") #strip() is more efficient
        line = line.strip() #strip removes everything unnecessary
        parts = line.split(";")
        if parts[0] == "id":
            continue
        name_dictionary[parts[0]] = [f"{parts[1]} {parts[2]}"]

exercise_dictionary = {}
with open(exercise_data) as exercise_file:
    for line in exercise_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        help_sum = 0
        for number in parts[1:]:
            help_sum += int(number)
        exercise_dictionary[parts[0]] = int(help_sum / 40 * 10)

exam_dictionary = {}
with open(exam_data) as exam_file:
    for line in exam_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        help_sum = 0
        for number in parts[1:]:
            help_sum += int(number)
        exam_dictionary[parts[0]] = help_sum

total = {}
for key, value in exercise_dictionary.items():
    if key in exam_dictionary:
        total[key] = value + exam_dictionary[key]

for key, value in name_dictionary.items():
    if key in total:
        if total[key] in range(0,15):
            print(value[0], 0)
        elif total[key] in range(15,18):
            print(value[0], 1)
        elif total[key] in range(18,21):
            print(value[0], 2)
        elif total[key] in range(21,24):
            print(value[0], 3)
        elif total[key] in range(24,28):
            print(value[0], 4)
        elif total[key] >= 28:
            print(value[0], 5)