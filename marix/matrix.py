input_list = [[1, 2, 3], [6, 5, 8], [7, 4, 9]]
 
 
def get_index(matrix) -> tuple:
    x = -1
    y = -1
    for col_index in matrix:
        x += 1
        for row_index in col_index:
            y += 1
            if row_index == min(col_index):
                row_list = []
                for i in range(0, len(matrix)):
                    row_list.append(matrix[i][y])
                if matrix[x][y] == max(row_list):
                    return x, y
            if y == (len(matrix) - 1):
                y = -1
        if x == (len(matrix) - 1):
            x = -1
 
 
print(get_index(input_list))
