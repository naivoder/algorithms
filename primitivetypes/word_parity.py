"""
this file checks the parity of a binary word, i.e. if the number of bits set to '1' is odd -> the parity = 1
parity checks are used to detect single bit errors in data storage and communication

problem: how to compute parity of large number of 64 bit words?

two keys to performing a large number of bit computations:
    1) process multiple bits at a time
    2) cache results in lookup table

caching: cannot store parity of every 64 bit integer, would need 2 ^ 64 storage
    - can group bits into 4 nonoverlapping 16 bit subwords (2 ^ 16 is comparitively small)
    - compute parity of each subword, compute parity of four results

"""
import random

# O(n) time complexity, n = word size
def brute_force(word:int=None) -> bool:
    if word is None:
        try:
            word = int(input("Enter a positive integer: "))
            if word <= 0:
                print("POSITIVE integer, please...")
                brute_force()
        except ValueError:
            print("Invalid number, try again please...")
            brute_force()
    parity = 0
    # while len(binary_word) > 0
    while word:
        # parity (xor) (least sig bit is 0 or 1)
        # if parity = 0, and bit is 1 -> parity = 1 (number of '1' bits is odd...)
        # if parity = 1, and bit is 1 -> parity = 0 (number of '1' bits is even...)
        parity ^= word & 1
        # right shift word by 1 bit
        # most sig bit = 0, new least sig bit to test
        word >>= 1
    return True if parity else False

# improve best and average cases -> erase lowest set bit in word
# O(k) time complexity, k = number of '1' bits in word
def erase_lowest(word:int=None) -> bool:
    if word is None:
        try:
            word = int(input("Enter a positive integer: "))
            if word <= 0:
                print("POSITIVE integer, please...")
                erase_lowest()
        except ValueError:
            print("Invalid number, try again please...")
            erase_lowest()
    parity = 0
    # there are still '1' bits to be counted
    while word:
        # if parity = 0 -> parity = 1 (0 + 1 = odd)
        # if parity = 1 -> parity = 0 (1 + 1 = even)
        parity ^= 1
        # drop the lowest '1' bit from the word
        word &= (word - 1)
    return True if parity else False

# O(n/L) time complexity, n = word size, L = width of word cache (16)
_16_bit_lkup = [erase_lowest(int) for int in range(2 ** 16)]
_test_data = [random.randint((2**62),(2**64)) for int in range(50)]
def cache_table(word:int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (_16_bit_lkup[word >> 3 * mask_size] \
          ^ _16_bit_lkup[(word >> 2 * mask_size) & bit_mask] \
          ^ _16_bit_lkup[(word >> mask_size) & bit_mask] \
          ^ _16_bit_lkup[word & bit_mask])

# compute parity of bits(x:x/2) and bits(x/2:0) until only one bit remains
# O(logn) time complexity, n = word size
def word_xor(word:int=None, word_size:int=64) -> int:
    if word is None:
        try:
            word = int(input("Enter a positive integer: "))
            if word <= 0:
                print("POSITIVE integer, please...")
                word_xor()
        except ValueError:
            print("Invalid number, try again please...")
            word_xor()
    while word_size > 1:
        word_size = int(word_size / 2)
        word ^= word >> word_size
        word_xor(word, word_size)
    return True if word else False

if __name__=="__main__":
    print("###---Brute Force---###")
    print(brute_force(4))
    print(brute_force())
    print("###---Drop Lowest---###")
    print(erase_lowest(4))
    print(erase_lowest())
    print("###---Cache Table---###")
    for test_case in _test_data:
        print(cache_table(test_case))
    print("###---Compare Half---###")
    print(word_xor(4))
    print(word_xor())
