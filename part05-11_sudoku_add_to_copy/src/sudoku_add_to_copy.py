#print_sudoku function from previous exercise for testing
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

# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
            new_sudoku.append(row[:]) #original changes without [:]

    new_sudoku[row_no][column_no] = number
    return new_sudoku

if __name__ == "__main__":
    example_sudoku  = [
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

    grid_copy = copy_and_add(example_sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(example_sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)