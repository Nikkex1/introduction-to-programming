# Write your solution here
def all_the_longest(list):
    new_list = []
    longest = len(list[0])
    for index in list:
        if len(index) > longest:
            longest = len(index)

    for index in list:
        if longest == len(index):
            new_list.append(index)
    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(all_the_longest(my_list))