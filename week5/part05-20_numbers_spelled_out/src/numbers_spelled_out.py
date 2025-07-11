# Write your solution here
def dict_of_numbers():
    lessthan10 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    ten_to_thirteen = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen"}
    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    number_dictionary = {}
    for key, value in lessthan10.items():
        number_dictionary[key] = value
    for key, value in ten_to_thirteen.items():
        number_dictionary[key] = value
    index = 4
    for number in range(14,20):
        if number == 15:
            number_dictionary[number] = "fifteen"
            index += 1
        elif number == 18:
            number_dictionary[number] = "eighteen"
            index += 1
        else:
            number_dictionary[number] = f"{lessthan10[index]}teen"
            index += 1
    index = 1
    for key, value in tens.items():
        if key % 10 == 0:
            number_dictionary[key] = value
        for number in range(1,10):
            number_dictionary[key + number] = value + f"-{lessthan10[index]}"
            index += 1
        index = 1


    print(number_dictionary)
    return number_dictionary


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])