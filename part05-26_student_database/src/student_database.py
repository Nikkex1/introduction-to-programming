# Write your solution here

#Add student
def add_student(database: dict, student: str):
    database[student] = [] #student as a key, list for value

#Print student
def print_student(database: dict, student: str):
    if student in database:
        print(f"{student}:")
        if len(database[student]) == 0:
            print(" no completed courses")
        else:
            grade_sum = 0 #helper variable for average grade
            course_list = {} #helper dictionary for duplicate courses
            last_grade = 0 #check whether duplicate grade is greater

            for item in database[student]: #item[0]: course name, item[1]: grade
                if item[1] > last_grade:
                    course_list[item[0]] = item[1]
                    last_grade = item[1]
                if item[0] not in course_list: #add courses that appear only once
                    course_list[item[0]] = item[1]

            print(f" {len(course_list)} completed courses:")
            for key, value in course_list.items():
                print(f"  {key} {value}") #course name + grade
                grade_sum += value
            print(f" average grade {grade_sum / len(course_list)}")

    else:
        print(f"{student}: no such person in the database")

#Add course
def add_course(database: dict, student: str, course: tuple):
    if course[1] != 0: #course[1] contains grade; 0 is skipped
        database[student].append(course)

#Summary
def summary(database: dict):

    number_of_students = len(database) #number of keys (=students)
    number_of_courses = {} #number of courses completed per student
    copy_list = [] #help list for duplicate courses
    count = 0 #help variable for counting distinct courses
    grade_dict = {}
    final = {}
    averages = {}

    for key, value in database.items():
        for item in value:
            if item[0] not in copy_list:
                copy_list.append(item[0])
                count += 1
        number_of_courses[key] = count
        count = 0

    for key, value in database.items():
        for item in value:
            if (key, item[0]) in grade_dict and item[1] > grade_dict[(key, item[0])]:
                grade_dict[(key, item[0])] = item[1]
            if (key, item[0]) not in grade_dict:
                grade_dict[(key, item[0])] = item[1]
            
    for key, value in grade_dict.items():
        if key[0] not in final: #create list
            final[key[0]] = []
        final[key[0]].append(value)
    for key in final: #sum the lists for each key
        final[key] = sum(final[key])

    for key, value in final.items():
        averages[key] = value / number_of_courses[key]
    
    print(f"students {number_of_students}")
    print(f"most courses completed {max(number_of_courses.values())} {max(number_of_courses, key=number_of_courses.get)}")
    print(f"best average grade {max(averages.values())} {max(averages, key=averages.get)}")
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)