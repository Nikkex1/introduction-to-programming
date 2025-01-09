# Write your solution here
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

            

if __name__ == "__main__":
    example_sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(example_sudoku, 0, 0))
    print(block_correct(example_sudoku, 1, 2))