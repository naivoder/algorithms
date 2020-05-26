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
    found = False; index = 1
    while not found:
        next_up = word + index
        next_weight = 0
        for bit in bin(next_up):
            if bit == '1':
                next_weight += 1
        if next_weight == weight:
            end = time.time() - start
            print('%s seconds!' % end)
            return next_up
        next_down = word - index
        next_weight = 0
        for bit in bin(next_down):
            if bit == '1':
                next_weight += 1
        if next_weight == weight:
            end = time.time() - start
            print('%s seconds!' % end)
            return next_down
        index += 1
    return found

def same_weight(word):
    start = time.time()
    num_bits = 64
    for index in range(num_bits - 1):
        if (word >> index) & 1 != (word >> (index + 1)) & 1:
            word ^= (1 << index) | (1 << (index + 1))
            end = time.time() - start
            print('%s seconds!' % end)
            return word

if __name__=='__main__':
    print('###---Swap Rightmost Different Bits---###')
    print(same_weight(2**25))
    user = input('Do you want to run the brute force version? ')
    if user in ['y', 'Y']:
        print('###---Brute Force Check Weights---###')
        print(brute_force(2**25))
    print(same_weight(2**25))
