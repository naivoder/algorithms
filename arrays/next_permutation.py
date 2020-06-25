"""
this file implements an algorithm that, given an array of integers, will return the next lexigraphical permutation of that array

for example, given the array [1, 2, 3, 1]
                    return = [1, 3, 1, 2]

"""

def next_perm(perm:list) -> list:
    # step backwards, find first decreasing number from the right
    pointer = len(perm) - 2
    while pointer >= 0 and perm[pointer] >= perm[pointer + 1]:
        pointer -= 1
    # if array is already largest permutation, return original
    if pointer == -1:
        return perm

    # swap with first entry from right greater than perm[pointer]
    for i in reversed(range(pointer + 1, len(perm))):
        if perm[i] > perm[pointer]:
            perm[pointer], perm[i] = perm[i], perm[pointer]
            break
    # reverse entries after pointer
    perm[pointer + 1:] = reversed(perm[pointer + 1:])
    return perm

if __name__=="__main__":
    print("###---Next Lexicographical Permutation---###")
    test_perm = [1, 2, 3, 1]
    print("Test permutation:", test_perm, end=" ")
    print("--> %s" % next_perm(test_perm))
