# Write your solution here
def longest_series_of_neighbours(list):
    longest = 1
    result = 1
    for i in range(1, len(list)):
        if abs(list[i - 1] - list[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
    return longest

if __name__ == "__main__":
    my_list = [1, 2]
    print(longest_series_of_neighbours(my_list))