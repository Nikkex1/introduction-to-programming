# Write your solution here
with open("diary.txt", "a") as my_file:
    while True:
        print("1- add an entry, 2 - read entries, 0 -quit")
        command = int(input("Function"))
        if command == 1:
            entry = input("Diary entry:")
            my_file.write(f"{entry}\n")
            print("Diary saved")
        elif command == 2:
            my_file = open("diary.txt") #makes the file readable again
            for line in my_file:
                print(line)
        elif command == 0:
            print("Bye now!")
            break