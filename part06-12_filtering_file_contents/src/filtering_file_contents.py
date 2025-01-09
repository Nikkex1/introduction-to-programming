# Write your solution here
def filter_solutions():
    with open("correct.csv", "w") as new_correct: #clears the file
        pass
    with open("incorrect.csv", "w") as new_incorrect:
        pass
    with open("solutions.csv") as my_file:
        for line in my_file:
            line = line.strip()
            line = line.split(";")
            new_correct = open("correct.csv", "a")
            new_incorrect = open("incorrect.csv", "a")
            if "+" in line[1]:
                parts = line[1].split("+")
                if int(parts[0]) + int(parts[1]) == int(line[2]):
                    new_correct.write(f"{line[0]};{line[1]};{line[2]}\n")
                else:
                    new_incorrect.write(f"{line[0]};{line[1]};{line[2]}\n")
            elif "-" in line[1]:
                parts = line[1].split("-")
                if int(parts[0]) - int(parts[1]) == int(line[2]):
                    new_correct.write(f"{line[0]};{line[1]};{line[2]}\n")
                else:
                    new_incorrect.write(f"{line[0]};{line[1]};{line[2]}\n")

if __name__ == "__main__":
    filter_solutions()