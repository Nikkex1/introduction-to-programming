# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for m_element in row:
            if m_element == element:
                count += 1

    return(count)

if __name__ == "__main__":
    example_matrix = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(example_matrix,1))