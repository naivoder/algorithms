"""
this file implements an algorithm to rotate a given matrix by pi (clockwise) in place using a four-way exchange of values
the method requires O(n2) time complexity but only O(1) additional space

"""

def rotate_matrix(square):
    size = len(square) - 1
    for i in range(len(square) // 2):
        for j in range(i, size - i):
            # perform 4-way exchange of values
            square[i][j], square[~j][i], square[~i][~j], square[j][~i] = square[~j][i], square[~i][~j], square[j][~i], square[i][j]
    return square

class RotatedMatrix:
    def __init__(self, square_matrix):
        self._square = square_matrix
    def read_entry(self, i, j):
        return self._square[~j][i]
    def write_entry(self, i, j, v):
        self._square[~j][i] = v

if __name__=="__main__":
    print("###---Rotate Matrix---###")
    test_matrix = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    print("Input matrix:")
    [print(row) for row in test_matrix]
    print("Rotate 90:")
    result_matrix = rotate_matrix(test_matrix)
    [print(row) for row in result_matrix]
