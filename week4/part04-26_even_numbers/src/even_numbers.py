# Write your solution here
def even_numbers(list):
    index = 0
    new_list = []
    while index < len(list):
        if list[index] % 2 == 0:
            new_list.append(list[index])
        index += 1
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(f"original {my_list}")
    print(f"new {even_numbers(my_list)}")