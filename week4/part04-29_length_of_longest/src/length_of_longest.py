# Write your solution here
def length_of_longest(list):
    longest = len(list[0])
    for index in list:
        if len(index) > longest:
            longest = len(index)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(length_of_longest(my_list))