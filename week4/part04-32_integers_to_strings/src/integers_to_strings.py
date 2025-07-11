# Write your solution here
def formatted(list):
    formatted_list = []
    for i in list:
        i = f"{i:.2f}"
        formatted_list.append(i)
    return formatted_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    print(formatted(my_list))