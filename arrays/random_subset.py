"""
this file implements an algorithm to generate a random subset of size k, given a range of size n
to do this efficiently, a hash table is used to map random values to their index
if the value already exists in the table, the previous index is stored as the new value

"""

import random

def random_subset(n, k, debug=False):
    hash = {}
    for i in range(k):
        # generate random index between i and n-1
        random_i = random.randrange(1, n)
        if debug:
            print("Random index:", random_i)
        # if already stored take stored value, else take self
        random_i_mapped = hash.get(random_i, random_i)
        i_mapped = hash.get(i, i)
        # store collected values in hash
        hash[random_i] = i_mapped
        hash[i] = random_i_mapped
        if debug:
            for key, value in hash.items():
                print(key, '->', value)
    return [hash[i] for i in range(k)]

if __name__=="__main__":
    print("###---Random Subset---###")
    print(random_subset(20, 5, debug=True))
    