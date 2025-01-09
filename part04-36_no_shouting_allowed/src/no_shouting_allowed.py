# Write your solution here
def no_shouting(list):
    new_list = []
    for word in list:
        if word.isupper() == False:
            new_list.append(word)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    print(no_shouting(my_list))