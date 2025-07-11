# Copy here code of line function from previous exercise
def line(integer, string):
    if len(string) > 1:
        print(integer * string[0])
    elif string == "":
        print(integer * "*")
    else:
        print(integer * string)

def triangle(size):
    # You should call function line here with proper parameters
    times = 1
    while times <= size:
        line(times, "#")
        times += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
