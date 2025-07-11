# Write your solution here
def distinct_numbers(list):
    new_list = []
    for index in list:
        if index not in new_list:
            new_list.append(index)
    return sorted(new_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))