# Write your solution here
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
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(column_correct(example_sudoku, 0))