# Write your solution here
def line(integer, string):
    if len(string) > 1:
        print(integer * string[0])
    elif string == "":
        print(integer * "*")
    else:
        print(integer * string)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "LOL")