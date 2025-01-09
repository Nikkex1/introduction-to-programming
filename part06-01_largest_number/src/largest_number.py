# write your solution here
def largest():
    list = []
    with open("numbers.txt") as new_file:
        for item in new_file:
            item = item.replace("\n", "") #remove empty lines
            list.append(int(item))
    return max(list)
if __name__ == "__main__":
    print(largest())