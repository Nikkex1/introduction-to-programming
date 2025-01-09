# Write your solution here
from string import ascii_letters, digits, whitespace

def change_case(orig_string: str):
    reverse_case = "" #strings are immutable
    for char in orig_string:
        if char == char.lower():
            reverse_case += char.upper()
        elif char == char.upper():
            reverse_case += char.lower()
        else:
            reverse_case += char

    return reverse_case

def split_in_half(orig_string: str):
    length = len(orig_string)
    split_tuple = (orig_string[0:int(length/2)]),(orig_string[int(length/2):])
    
    return split_tuple

def remove_special_characters(orig_string: str):
    specials_removed = ""
    allowed = ascii_letters + digits + whitespace
    for char in orig_string:
        if char in allowed:
            specials_removed += char

    return specials_removed

if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)