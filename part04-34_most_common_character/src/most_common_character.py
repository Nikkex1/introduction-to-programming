# Write your solution here
def most_common_character(string):
    count = 0
    common_char = ""
    for char in string:
        if string.count(char) > count:
            count = string.count(char)
            common_char = char
    return common_char

if __name__ == "__main__":
    example_string = "abcdbde"
    print(most_common_character(example_string))