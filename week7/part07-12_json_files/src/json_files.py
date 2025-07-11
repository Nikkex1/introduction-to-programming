# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read() #store the file in data

    people = json.loads(data)
    for person in people:
        print(f"{person["name"]} {person["age"]} years (",end="")
        print(*person["hobbies"], sep = ", ", end="")
        print(")")

if __name__ == "__main__":
    print_persons("file1.json")