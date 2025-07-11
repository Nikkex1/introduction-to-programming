# Write your solution here
def spruce(size):
    print("a spruce!")
    times = 1
    helper = 1
    while times <= size:
        print(" " * (size - times) + "*" * (helper))
        times += 1
        helper += 2
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(8)