# Write your solution here
def list_sum(list1, list2):
    new_list = []
    help_index = 0
    for index in list2:
        new_list.append(index + list1[help_index])
        help_index += 1
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))