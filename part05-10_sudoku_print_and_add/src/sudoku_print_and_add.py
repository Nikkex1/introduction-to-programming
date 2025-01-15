# Write your solution here
def print_sudoku(sudoku: list):
    element_count = 0
    row_count = 1 #start at row 1
    for row in sudoku:
        for element in row:
            if element != 0 and element_count < 9:
                print(element, end="")
                element_count += 1
            if element == 0 and element_count < 9:
                print("_", end="") #replace 0 with _
                element_count += 1
            if element_count == 3 or element_count == 6:
                print(" ", end="") #add empty space after 3rd and 6th _
            if element_count < 9:
                print(" ", end="") #add empty space after _
            if element_count == 9:
                print()
                if row_count % 3 == 0 and row_count != 9:
                    print()
                element_count = 0
                row_count += 1
    return sudoku
    #

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
    
    return sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)