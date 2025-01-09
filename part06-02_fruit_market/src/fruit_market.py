# write your solution here
def read_fruits():
    dictionary = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            item = line.split(";")
            dictionary[item[0]] = float(item[1])

    return dictionary

if __name__ == "__main__":
    print(read_fruits())