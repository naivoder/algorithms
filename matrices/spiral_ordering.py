"""
this file implements two methods to compute the clockwise spiral ordering of an (n x n) matrix

"""

def spiral_ordering(square_matrix):
    def _add_layer(offset):
        # location is center tile of odd matrix
        if offset == len(square_matrix) - offset - 1:
            spiral.append(square_matrix[offset][offset])
            return
        # flatten four sides of spiral layer
        spiral.extend(square_matrix[offset][offset:-1 - offset])
        spiral.extend(list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral.extend(square_matrix[-1 - offset][-1 - offset:offset:-1])
        spiral.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])
    spiral = []
    for offset in range((len(square_matrix) + 1) // 2):
        _add_layer(offset)
    return spiral

def quick_spiral(square_matrix):
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral = []
    for i in range(len(square_matrix)**2):
        spiral.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        if (next_x not in range(len(square_matrix)) or next_y not in range(len(square_matrix)) or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral

if __name__ == "__main__":
    test_matrix = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    print("###---Spiral Ordering---###")
    print("Matrix:")
    [print(row) for row in test_matrix]
    print("Flattened:")
    print(spiral_ordering((test_matrix)))
    print(quick_spiral((test_matrix)))

