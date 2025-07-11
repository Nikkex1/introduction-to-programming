# Write your solution here
def filter_incorrect():
    with open("correct_numbers.csv", "w") as correct_file:
        pass
    lottery_dict = {}
    temp_dict = {}
    with open("lottery_numbers.csv") as lottery_file:
        for line in lottery_file:
            line = line.strip()
            parts = line.split(";")
            weeks = parts[0].split(" ") #week, number
            numbers = parts[1].split(",") #lottery numbers
            try:
                temp_dict[weeks[0],int(weeks[1])] = numbers #key: week, value: numbers
            except ValueError:
                pass

    for key, value in temp_dict.items():
            try:
                #line = (f"{key[0]} {int(key[1])};{int(value[0])},{int(value[1])},{int(value[2])},{int(value[3])},{int(value[4])},{int(value[5])},{int(value[6])}")
                lottery_dict[key[0], int(key[1])] = [int(value[0]),int(value[1]),int(value[2]),int(value[3]),int(value[4]),int(value[5]),int(value[6])]
            except ValueError:
                pass #incorrect numbers
            except IndexError:
                pass #too few number

    temp_dict.clear() #clear the temporary dictionary for further use
    for key, value in lottery_dict.items():
        for item in value:
            if item not in range(40):
                temp_dict[key] = value #find items out of range
    for key in temp_dict:
        del lottery_dict[key] #delete items that are out of range

    temp_dict.clear()
    occurance = [0] * 39
    for key, value in lottery_dict.items():
        occurance = [0] * 39
        for item in value:
            occurance[item] += 1
        if 2 in occurance:
            temp_dict[key] = value
    for key in temp_dict:
        del lottery_dict[key] #delete keys with duplicate numbers

    with open("correct_numbers.csv", "a") as correct_file:
        for key, value in lottery_dict.items():
            line = f"{key[0]} {key[1]};{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}\n"
            correct_file.write(line)
if __name__ == "__main__":
    filter_incorrect()