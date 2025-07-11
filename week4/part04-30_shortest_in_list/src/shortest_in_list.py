# Write your solution here
def shortest(list):
    shortest = list[0]
    for index in list:
        if len(index) < len(shortest):
            shortest = index
    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(shortest(my_list))