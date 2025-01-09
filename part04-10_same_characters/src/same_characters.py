# Write your solution here
def same_chars(string, int1, int2):
    if string[int1:int1 + 1] == string[int2:int2 + 1]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))