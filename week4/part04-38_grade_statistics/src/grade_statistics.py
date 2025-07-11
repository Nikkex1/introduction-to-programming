# Write your solution here

#Input for exam points and exercises completed, separated into lists.
exam_points = []
exercises_completed = []

while True:
    intial_input = input("Exam points and exercises completed:")
    if intial_input == "":
        break
    split_list = intial_input.split()
    for number in range(len(split_list)):
        split_list[number] = int(split_list[number])
    exam_points.append(split_list[0])
    exercises_completed.append(split_list[1])

#Conversion of completed exercises into points, rounded down.
extra_points = [x / 10 for x in exercises_completed]
extra_points = [int(x) for x in extra_points]

#Total points from exam and exercises.
total_points = []
for i in range(len(exam_points)):
    total_points.append(exam_points[i] + extra_points[i])

#Grades; list for grades in range of 0-5 and helper index to check for <10 exam points.
grades_list = [0, 0, 0, 0, 0, 0]
grade_index = 0

for grade in total_points:
    if grade in range(0,15) or exam_points[grade_index] < 10:
        grades_list[0] += 1
        grade_index += 1
    elif grade in range(15,18) and exam_points[grade_index] >= 10:
        grades_list[1] += 1
        grade_index += 1
    elif grade in range(18,21) and exam_points[grade_index] >= 10:
        grades_list[2] += 1
        grade_index += 1
    elif grade in range(21,24) and exam_points[grade_index] >= 10:
        grades_list[3] += 1
        grade_index += 1
    elif grade in range(24,27) and exam_points[grade_index] >= 10:
        grades_list[4] += 1
        grade_index += 1
    elif grade in range(27,31) and exam_points[grade_index] >= 10:
        grades_list[5] += 1
        grade_index += 1

#Number of students who passed
success = sum(grades_list) - grades_list[0]

#Final print()
print("Statistics:")
print(f"Points average: {(sum(total_points) / len(total_points)):.1f}")
print(f"Pass percentage: {(success / sum(grades_list) * 100):.1f}")
print("Grade distribution:")
stat_index = 5
star_index = 5
for x in grades_list:
    print(f"  {stat_index}: {grades_list[star_index] * "*"}")
    stat_index -= 1
    star_index -= 1