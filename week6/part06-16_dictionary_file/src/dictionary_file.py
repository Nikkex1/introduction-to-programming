# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    command = int(input("Function: "))
    if command == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        line = f"{finnish};{english}\n"
        with open("dictionary.txt", "a") as dictionary_file:
            dictionary_file.write(line)
        print("Dictionary entry added")
    elif command == 2:
        search = input("Search term: ")
        with open("dictionary.txt", "r") as dictionary_file:
            for line in dictionary_file:
                line = line.strip()
                line = line.split(";")
                if search in line[0] or search in line[1]:
                    print(f"{line[0]} - {line[1]}")
    elif command == 3:
        print("Bye!")
        break