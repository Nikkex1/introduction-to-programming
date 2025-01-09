# Write your solution here
def sum_of_positives(list):
    index = 0
    sum = 0
    while index < len(list):
        if list[index] > 0:
            sum += list[index]
        index += 1
    return sum

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print(f"The result is {result}")