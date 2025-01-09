# write your solution here
def matrix_sum():
    sum_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "") #remove empty lines
            item = line.split(",")
            for val in item:
                sum_list.append(int(val))
        return sum(sum_list)

def matrix_max():
    max_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "") #remove empty lines
            item = line.split(",")
            for val in item:
                max_list.append(int(val))
        return max(max_list)
    
def row_sums():
    row_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "") #remove empty lines
            item = line.split(",")
            for val in item:
                row_list[index] += int(val)
            index += 1
    return row_list

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())