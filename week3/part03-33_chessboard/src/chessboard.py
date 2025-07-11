# Write your solution here
def chessboard(length):
    i = 1
    while i <= length:
        if i % 2 != 0:
            print(str("10" * length)[0:length])
            i += 1
            continue
        if i % 2 == 0:
            print(str("01" * length)[0:length])
            i += 1
# Testing the function
if __name__ == "__main__":
    chessboard(4)
