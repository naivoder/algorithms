"""
this file takes as input a 64-bit word and swaps bits 'i' and 'j'

"""
# brute force assignment: bit_i = (word >> i) & 1

# a brute force approach would consist of saving bits i and j into memory and reassigning them
# since a bit only has two values, an initial check for similarity eliminates unnecessary work
# O(1) time complexity (regardless of word size!) using bit fiddling techniques rather than object swap
def swap_bits(word, i, j):
    #extract bits i and j and compare
    if (word >> i) & 1 != (word >> j) & 1:
        # case 1 - bits differ
        # bitmask logic: send opposite bit to position
        # e.g. word = 11 (1011), i = 1, j = 2
        # bitmask = (0010) | (0100) = (0110)
        bit_mask = (1 << i) | (1 << j)
        # word xor bitmask
        word ^= bit_mask
    return word

if __name__=="__main__":
    word = 1111
    print("###---Bit Swapping---###")
    print("Word:", word)
    print("Binary:", bin(word))
    print("Swapping bits 2 & 3")
    new_word = swap_bits(word, 2, 3)
    print("Word:", new_word)
    print("Binary:", bin(new_word))
