# Write your solution here
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

if __name__ == "__main__":
    example_sudoku = [
  [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
  [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
  [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
  [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # row 3
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
  [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
  [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
  [ 3, 0, 0, 0, 0, 0, 3, 0, 2 ]]   # row 8
    print(row_correct(example_sudoku, 0))
    print(row_correct(example_sudoku, 1))
    print(row_correct(example_sudoku, 2))
    print(row_correct(example_sudoku, 3))
    print(row_correct(example_sudoku, 4))
    print(row_correct(example_sudoku, 5))
    print(row_correct(example_sudoku, 6))
    print(row_correct(example_sudoku, 7))
    print(row_correct(example_sudoku, 8))