# Copy here code of line function from previous exercise and use it in your solution
def line(integer, string):
    if len(string) > 1:
        print(integer * string[0])
    elif string == "":
        print(integer * "*")
    else:
        print(integer * string)

def shape(size, triangle_char, rectangle_height, rectangle_char):
    times = 1
    while times <= size:
        line(times, triangle_char)
        times += 1
    times = 1
    while times <= rectangle_height:
        line(size, rectangle_char)
        times += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")