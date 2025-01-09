# Write your solution here
from string import ascii_lowercase, digits
from random import choice, shuffle

def generate_strong_password(length: int, numbers: bool, specials: bool):
    counts = [0,0,0]
    password = ""
    pool = ascii_lowercase
    special_chars = "!?=+-()#"
    if numbers == True:
        pool += digits
    if specials == True:
        pool += special_chars
    while True:
        password += choice(pool)
        if len(password) == length:
            for char in password:
                if char in ascii_lowercase:
                    counts[0] += 1
                elif char in digits:
                    counts[1] += 1
                else:
                    counts[2] += 1
            if counts[0] == 0:
                password = ""
                counts = [0,0,0]
                continue
            if counts[1] == 0 and numbers == True:
                password = ""
                counts = [0,0,0]
                continue
            if counts[2] == 0 and specials == True:
                password = ""
                counts = [0,0,0]
                continue
            break

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))