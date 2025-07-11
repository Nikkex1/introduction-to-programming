# Write your solution here
import csv
from difflib import get_close_matches

if True:
    text = input("Write text:")
else:
    text = "This is an example text wiht some erors"

original_text = text.split(" ")

checklist = []
with open("wordlist.txt") as list_of_words:
    for line in csv.reader(list_of_words): #line: list
        checklist.append(line[0]) #line[0]: str

suggestions = []
for word in original_text:
    if word.lower() in checklist: #word is correct
        print(f"{word} ",end="")
    else:
        print(f"*{word}* ",end="") #word is misspelled
        suggestions.append(word)
print() #new line after end=""
print("suggestions:")
for item in suggestions:
    x = get_close_matches(item, checklist)
    print(f"{item}: ",end="")
    print(*x, sep=", ") #does not work in f-strings