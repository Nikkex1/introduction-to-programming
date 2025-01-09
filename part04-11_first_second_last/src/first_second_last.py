# Write your solution here
def first_word(string1):
    index1 = string1.find(" ") #find first whitespace
    return string1[0:index1] #return first word from start to first whitespace

def second_word(string2):
    index1 = string2.find(" ") #find first whitespace again
    index2 = string2.find(" ", index1 + 1) #find second whitespace
    if string2[index2] == " ": #if second whitespace exists (= more than two words):
        return string2[index1 + 1:index2] #return second word from first whitespace to second whitespace
    else: #if there is no second whitespace (= only two words):
        return string2[index1 + 1:len(string2)] #return second word from first whitespace to the end of the sentence

def last_word(string3):
    index3 = -1 #last index of the sentence
    while string3[index3] != " ":
        index3 -= 1 #index3 - 1 until the last whitespace is found
    return string3[index3 + 1:len(string3)] #return last word from last whitespace to the end of the sentence

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))