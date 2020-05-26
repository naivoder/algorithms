"""
defining the weight of an integer to be the number of bits set to '1' in it's binary representation...
the challenge is to write a program that computes the closest integer with the same binary weight

eg. 1011 (11) -> weight = 3
    0111  (7) -> weight = 3

the brute force solution is the to test the weight of every number
the secret trick is to flip the rightmost two bits that differ (i.e. example above)

"""
import time

def brute_force(word):
    start = time.time()
    weight = 0
    for bit in bin(word):
        if bit == '1':
            weight += 1
    found = False; i = 1
    while not found:
        next_up = word + i
        next_weight = 0
        for bit in bin(next_up):
            if bit == '1':
                next_weight += 1
        if next_weight == weight:
            end = time.time() - start
            print("%s seconds!")
            return next_up
        next_down = word - i
        next_weight = 0
        for bit in bin(next_down):
            if bit == '1':
                next_weight += 1
        if next_weight == weight:
            end = time.time() - start
            print("%s seconds!" % end)
            return next_down
        i += 1

if __name__ == "__main__":
    user = input('Do you want to run the brute force version? ')
    if user in ['y', 'Y']:
        print(brute_force(2**25))
