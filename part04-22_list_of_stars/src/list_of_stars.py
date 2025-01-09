# Write your solution here
def list_of_stars(list):
    index = 0
    while index < len(list):
        print(f"{list[index] * "*"}")
        index += 1

if __name__ == "__main__":
    print(list_of_stars([3, 7, 1, 1, 2]))