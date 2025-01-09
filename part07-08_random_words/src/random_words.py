# Write your solution here
from random import shuffle

def words(n: int, beginning: str):
    found_words = []
    with open("words.txt") as word_file:
        for line in word_file:
            line = line.strip()
            if line.startswith(beginning):
                found_words.append(line)

    if len(found_words) < n:
        raise ValueError
    shuffle(found_words)
    final = []
    for i in range(n):
        final.append(found_words[i])

    return final

if __name__ == "__main__":
    word_list = words(2, "car")
    for word in word_list:
        print(word)