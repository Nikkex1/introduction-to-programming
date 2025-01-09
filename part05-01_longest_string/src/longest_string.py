# Write your solution here
def longest(strings: list):
    help_list = []
    for word in strings:
        help_list.append(len(word))
    longest_word = help_list.index(max(help_list))
    return strings[longest_word]

if __name__ == "__main__":
    string_list = ["first word","second","third152"]
    print(longest(string_list))