# Write your solution here
def histogram(string: str):
    char_dictionary = {}
    for char in string:
        if char not in char_dictionary:
            char_dictionary[char] = 0
        char_dictionary[char] += 1

    for key, value in char_dictionary.items():
        print(key,"*"*value)

if __name__ == "__main__":
    print(histogram("abba"))