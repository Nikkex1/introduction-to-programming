# Write your solution here
def everything_reversed(list):
    reversed_list = []
    for string in list:
        reversed_list.append(string[::-1])
    reversed_list.reverse()
    return reversed_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    print(everything_reversed(my_list))