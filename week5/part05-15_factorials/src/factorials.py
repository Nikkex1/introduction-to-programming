# Write your solution here
def factorials(n: int):
    dictionary = {}
    prevN = 1
    for i in range(1,n+1):
        prevN *= i
        dictionary[i] = 1 * prevN

    print(dictionary)
    return dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])