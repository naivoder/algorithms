"""
this file implements an algorithm to compute the first n rows of pascals triangle
pascals triangle has layers of increasing size where each entry is the sum of the adjacent entries above it
ex:
     1
    1 1
   1 2 1

"""

def pascals_triangle(num_rows):
    # initialize triangle with 1s
    result = [[1] * (i + 1) for i in range(num_rows)]
    for i in range(num_rows):
        # avoids first two rows
        for j in range(1, i):
            # set entry to be sum of above adjacent entries (j-1) and (j)
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    # find len of last row
    spacing = len(result[num_rows - 1])

    for i in range(num_rows):
        print(" " * spacing, result[i])
        spacing -= 1

if __name__=="__main__":
    print("###---Pascal's Triangle---###")
    rows = int(input("How many rows would you like to display? "))
    pascals_triangle(rows)