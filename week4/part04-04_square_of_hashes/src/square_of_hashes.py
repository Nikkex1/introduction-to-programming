# Copy here code of line function from previous exercise
def line(integer, string):
    if len(string) > 1:
        print(integer * string[0])
    elif string == "":
        print(integer * "*")
    else:
        print(integer * string)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    times = 1
    while times <= size:
        line(size, "#")
        times += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
