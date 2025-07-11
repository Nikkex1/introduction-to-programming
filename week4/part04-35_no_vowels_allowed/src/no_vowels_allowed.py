# Write your solution here
def no_vowels(string):
    new_string = string
    vowels = ["a", "e", "i", "o", "u"]

    for char in vowels:
        new_string = new_string.replace(char, "")

    return new_string

if __name__ == "__main__":
    example_string = "this is an example"
    print(no_vowels(example_string))