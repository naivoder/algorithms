"""
compute random permutation by applying offline sampling method to entire list
offline sampling generates random index between (position, length(array)) for swap at every position

"""

from offline_sampling import random_sample

def compute_random_permutation(n):
    permutation = list(range(n))
    random_sample(permutation, n)
    return permutation

if __name__=="__main__":
    n = 10
    print(list(range(n)))
    print(compute_random_permutation(n))