# Write your solution here
def squared(string, number):
    i = 1
    help_string = string * 10000
    x = 0
    y = number
    while i <= number:
        print(help_string[x:y])
        i += 1
        x += number
        y += number
        

if __name__ == "__main__":
    squared("python", 15)