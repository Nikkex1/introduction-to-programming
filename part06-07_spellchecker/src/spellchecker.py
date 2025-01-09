# write your solution here
if True:
    text = input("Write text:")
else:
    text = "This is an example text wiht some erors"

original_text = text.split(" ")

checklist = []
with open("wordlist.txt") as list_of_words:
    for line in list_of_words:
        line = line.strip()
        checklist.append(line)

for word in original_text:
    if word.lower() in checklist:
        print(f"{word} ",end="")
    else:
        print(f"*{word}* ",end="")