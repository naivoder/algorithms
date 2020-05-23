"""
this file implements two handy bit manipulations, mainly so that I don't forget how they work

"""

# handy tricks:
# x & (x-1) --> clears lowest set bit in 'x'
# x & ~(x-1) --> extracts lowest set bit in 'x'

def tricks():
    print('x & (x-1) --> x=16')
    print('16 base 2:', bin(16))
    print('%s = 16 & (15)' % (bin(16&15)))

    print('x & ~(x-1) --> x=11')
    print('11 base 2:', bin(11))
    print('%s = 11 & ~(10)' % (bin(11&~10)))

if __name__=="__main__":
    tricks()
