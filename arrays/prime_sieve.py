"""
this file implements an algorithm to generate all primes up to a given (n)

rather than using a brute force method to check each number, a hash is initialized to True and for each prime number discovered its multiples are subsequently set to False
this technique is known as a sieve. slight improvements can be made by storing only odd numbers and sieving from num^2 however time and space complexity overall do not change.

"""

def generate_primes(up_to:int) -> list:
    if up_to < 2:
        return []
    primes = []
    # initialize array to True, except for 0 and 1
    is_prime = [False, False] + [True] * (up_to - 1)
    # up_to + 1 required for 'up to and including'
    for num in range(2, up_to + 1):
        if is_prime[num]:
            primes.append(num)
            for i in range(num * 2, up_to + 1, num):
                is_prime[i] = False
    return primes

if __name__=="__main__":
    print("###---Generating Primes---###")
    user_in = int(input("Upper limit? "))
    print(generate_primes(user_in))
