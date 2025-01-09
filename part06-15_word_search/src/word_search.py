# Write your solution here
def find_words(search_term: str):
    found_words = []
    with open("words.txt") as world_list:
        for line in world_list:

            line = line.strip()
            index = 0
            correct = 0

            if "." in search_term and len(line) == len(search_term):
                for char in line:
                    if char == search_term[index] or search_term[index] == ".":
                        index +=1
                        correct += 1
                    else:
                        index += 1
                        correct = 0

                    if correct == len(line):
                        found_words.append(line)

            elif "*" in search_term:
                if line.endswith(search_term[1:]): #ends with *string
                    found_words.append(line)
                elif line.startswith(search_term[:-1]): #starts with string*
                    found_words.append(line)
            elif search_term == line:
                found_words.append(line)

    return found_words

if __name__ == "__main__":
    print(find_words("ca.."))