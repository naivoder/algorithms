"""
working on the count_bits file, I realised I had a poor understanding of bitwise operations
this file is my attempt to remedy that via some basic tutorial-like operations
the function accepts a vector of any length, and assumes the final value should be used as the return
by default the first two values in the vector are selected for the operations
a helper function maintains reader-friendly command line output

"""

a = 60      # 0011 1100
b = 13      # 0000 1101
c = 0       # 0000 0000
vector = [a, b, c]

def neg(number):
    return ' ' if number >= 0 else ''

def basic_ops(vector, a=0, b=1):
    print("###---Basic Bitwise Operations---###")
    print("A: %s = %s   B: %s = %s" % (vector[a], bin(vector[a]), vector[b], bin(vector[b])))
    # (& and)   12 = 0000 1100
    vector[-1] = vector[a] & vector[b]
    print("1)  A & B: C = ", neg(vector[-1]), vector[-1], neg(vector[-1]), bin(vector[-1]))

    # (| or)    61 = 0011 1101
    vector[-1] = vector[a] | vector[b]
    print("2)  A | B: C = ", neg(vector[-1]), vector[-1], neg(vector[-1]), bin(vector[-1]))

    # (^ xor)   49 = 0011 0001
    vector[-1] = vector[a] ^ vector[b]
    print("3)  A ^ B: C = ", neg(vector[-1]), vector[-1], neg(vector[-1]), bin(vector[-1]))

    # (~ 1cmp) -61 = 0011 0001 --> flip bits!
    vector[-1] = ~vector[a]
    print("4)    ~ A: C = ", neg(vector[-1]), vector[-1], neg(vector[-1]), bin(vector[-1]))

    # (<< ls)  240 = 1111 0000 --> bit shift left
    vector[-1] = vector[a] << 2
    print("5) A << 2: C =", neg(vector[-1]), vector[-1], neg(vector[-1]), bin(vector[-1]))

    # (>> rs)   15 = 0000 1111 --> bit shift right
    vector[-1] = vector[a] << 2
    print("6) A >> 2: C =", neg(vector[-1]), vector[-1], neg(vector[-1]), bin(vector[-1]))

if __name__=="__main__":
    basic_ops(vector)
