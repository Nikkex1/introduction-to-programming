# Write your solution here
def read_input(input_string: str, min_number: int, max_number: int):
    while True:
        try:
            int_number = int(input(input_string))
            if int_number >= min_number and int_number <= max_number:
                return int_number
        except ValueError:
            pass
        print(f"You must type in an integer between {min_number} and {max_number}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)