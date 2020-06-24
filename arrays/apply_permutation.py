"""
this file implements an algorithm to apply a permutation to an array without the use of additional storage space
this is achieved in O(n) time by performing a series of swaps on both the permuted array and permutations simultaneously until  all p[i] = i

"""

def apply_permutation(perm:list, array:list) -> list:
    for i in range(len(array)):
        while perm[i] != i:
            array[perm[i]], array[i] = array[i], array[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return array

if __name__=="__main__":
    test_array = [1, 2, 3, 4, 5]
    test_perm  = [4, 3, 2, 1, 0]
    print("###---Apply Permutation---###")
    print(apply_permutation(test_perm, test_array))
    test_array = [1, 2, 3, 4, 5]
    test_perm  = [1, 0, 3, 4, 2]
    print(apply_permutation(test_perm, test_array))
    test_array = [1, 2, 3, 4, 5]
    test_perm  = [3, 4, 0, 1, 2]
    print(apply_permutation(test_perm, test_array))
