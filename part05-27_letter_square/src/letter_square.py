# Write your solution here
from string import ascii_uppercase

letters = {}
for i in range(26):
    letters[i] = ascii_uppercase[i]

if True:
    layers = int(input("Layers:"))
else: #for testing
    layers = 5

matrix = []
for i in range(layers): #create upper-left of the matrix
    matrix.append([])

row = 0
for sublist in matrix:
    for item in range(layers): # go though 0 - (layers-1) for each row
        if item < row:
            matrix[row].append(letters[layers-1-item])
        else:
            matrix[row].append(letters[layers-1-row]) #layers-1: last char
    row += 1

#The printout:
string = "" #for printing the matrix as a string
lower_half = matrix[::-1]
for item in matrix: #upper half
    upper_r = item[::-1]
    print(*item,sep="",end="")
    print(*upper_r[1:], sep="")
for item in lower_half: #lower half
    lower_r = item[::-1]
    if "A" in item:
        continue
    print(*item,sep="",end="")
    print(*lower_r[1:], sep="")

print(string)