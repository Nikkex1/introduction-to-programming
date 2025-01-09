# Write your solution here
import string

def separate_characters(my_string: str):
    first = ""
    second = ""
    third = ""
    for char in my_string:
        if char in string.ascii_letters:
            first += char
        elif char in string.punctuation:
            second += char
        else:
            third += char
            
    string_tuple = first, second, third
    return string_tuple

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])