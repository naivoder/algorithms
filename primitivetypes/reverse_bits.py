"""
problem: program takes 64 bit integer and returns a 64 bit integer consisting of bits in the reverse order

use 16 bit lookup table holding reversed bits for index, break input into 4 16 bit words, the solution will be the hashed value of the four words in reverse order
eg (4 bit lkup) word = 46617:
    ->    1011 0110 0001 1001
    ->    lkup[11] lkup[6] lkup[1] lkup[9]
    ->    reverse(1101 0110 1000 1001)
    ->    1001 1000 0110 1101
    ->    = 39021
NOTE: I spent well over an hour working on this thinking it was broken before I realized the numbers it was returning are Huge because the inputs I was giving it were so small (compared to 2 ** 64!). The solution above will be returned with an additional (16 * 3) trailing zeros!

"""

def build_table(word):
    i, j = 0, 15
    while i < j:
        if (word >> i) & 1 != (word >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            word ^= bit_mask
        i += 1; j -= 1
    # print(word)
    return word

def reverse_bits(word: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    a = (_lkup[word & bit_mask] << (3 * mask_size) \
    | _lkup[(word >> mask_size) & bit_mask] << (2 * mask_size) \
    | _lkup[(word >> (2 * mask_size)) & bit_mask] << mask_size \
    | _lkup[(word >> (3 * mask_size)) & bit_mask])
    return(a)

if __name__=="__main__":
    print("###---Reverse Bits---###")
    _lkup = [build_table(num) for num in range(2**16)]
    print(reverse_bits(46617))
    print(reverse_bits((2**64)), end=", ")
    print(reverse_bits((2**63)), end=", ")
    print(reverse_bits((2**62)), end=", ")
    print(reverse_bits((2**61)), end=", ")
    print(reverse_bits((2**60)), end=", ")
    print(reverse_bits((2**59)), end=", ")
    print(reverse_bits((2**58)))
