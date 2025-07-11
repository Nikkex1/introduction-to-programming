#Row function
def row_correct(sudoku: list, row_no: int):
    help_list = [0,0,0,0,0,0,0,0,0] #list for numbers 1-9 of a row
    for element in sudoku[row_no]:
        if element != 0: #zeros of a row are not counted
            help_list[element-1] += 1
    #print(help_list)
    true_or_false = True
    for value in help_list:
        if value > 1:
            true_or_false = False

    return true_or_false

#Column function
def column_correct(sudoku: list, column_no: int):
    column_list = [] #list for extracting the column
    for row in sudoku:
        column_list.append(row[column_no])

    help_list = [0,0,0,0,0,0,0,0,0] #list for numbers 1-9
    for i in column_list:
        if i != 0:
            help_list[i-1] += 1

    true_or_false = True
    for value in help_list:
        if value > 1:
            true_or_false = False
    return true_or_false

#Block function
def block_correct(sudoku: list, row_no: int, column_no: int):
    grid_list = []
    row = 0
    column = 0
    while row < 3:
        grid_list.append(sudoku[row_no + row][column_no + column])
        column += 1
        if column == 3:
            row += 1
            column = 0

    help_list = [0,0,0,0,0,0,0,0,0] #list for numbers 1-9
    for i in grid_list:
        if i != 0:
            help_list[i-1] += 1

    true_or_false = True
    for value in help_list:
        if value > 1:
            true_or_false = False
    return true_or_false

# Write your solution here
def sudoku_grid_correct(sudoku: list):
    for test in range(0,9):
        if row_correct(sudoku,test) == False:
            print("row false")
            return False
        if column_correct(sudoku,test) == False:
            print("column false")
            return False
    for blocktest in range(0,9,3):
        if block_correct(sudoku,blocktest,blocktest) == False:
            print("block false")
            return False

    return True

if __name__ == "__main__":
    example_sudoku = [
  [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
  [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
  [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
  [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
  [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
  [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
  [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
  [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
  [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(example_sudoku))