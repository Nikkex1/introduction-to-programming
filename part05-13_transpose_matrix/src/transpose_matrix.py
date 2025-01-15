# Write your solution here
def transpose(matrix: list):
    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            new_matrix = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = new_matrix

if __name__ == "__main__":
    example_matrix = [[1,2],[1,2]]
    print(example_matrix)
    transpose(example_matrix)
    print(example_matrix)