"""
this file implements two solutions to determine whether a given matrix constitutes a valid sudoko game board
the first solution check rows, columns and sub-matrices explicitly, the second method uses list comprehensions

"""
from math import sqrt
from collections import Counter

def has_duplicate(block, debug=False):
    block = list(filter(lambda x: x != 0, block))
    if debug:
        print("Block:", block)
    return len(block) != len(set(block))

def is_valid_sudoku(partial):
    size = len(partial)

    # check rows and columns for duplicates
    if any(has_duplicate([partial[i][j] for j in range(size)]) or has_duplicate([partial[j][i] for j in range(size)]) for i in range(size)):
        return False

    # check sub-matrices for duplicates
    region = int(sqrt(size))
    return all(not has_duplicate([partial[a][b] for a in range(region * height, region * (height + 1))
                                                for b in range(region * width, region * (width + 1))])
                                                for height in range(region) for width in range(region))

# pythonic solution
def is_valid_pythonic(partial):
    region = int(sqrt(len(partial)))
    return max(Counter(k for i, row in enumerate(partial)
                         for j, col in enumerate(row) if col != 0
                         for k in ((i, str(col)), (str(col), j),
                                   (i // region, j //region, str(col)))).values(), default=0) <= 1

if __name__=="__main__":
    test_puzzle = [[1, 0, 2, 0],
                   [3, 0, 0, 1],
                   [0, 1, 3, 0],
                   [2, 3, 1, 0]]

    result = is_valid_sudoku(test_puzzle)
    print('*** Method 1 ***')
    print("Valid puzzle board!") if result else print("Not valid!")

    result = is_valid_pythonic(test_puzzle)
    print('*** Method 2 ***')
    print("Valid puzzle board!") if result else print("Not valid!")