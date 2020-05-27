"""
this file implements a method to multiply two non-negative integerrs without using arithmetic operators

the brute force solution would be to intialize result to 0 and add 'x' to it 'y' times. this would have runtime as high as O(2**n)
a better solution is to use bitwise operations, iterating through each bit of x and and adding (2**k)y if the kth bit of 'x' == 1
(2**k)y is calculated by left-shifting 'y' by 'k', since using arithmetic operators is forbidden, we must define an 'add' as well as a 'multiply'
the add works to 'carry' the remainder of two 1 bits to the next position

this algorithm was taken from EPI (Aziz, Lee, Prakash) and gives me a headache

"""
def add(x:int, y:int) -> int:
    if y == 0:
        return x
    else:
        return add(x ^ y, (x & y) << 1)

def multiply(x:int, y:int) -> int:
    sum = 0
    while x:
        if x & 1:
            sum = add(sum, y)
        x, y = x >> 1, y << 1
    return sum

if __name__=="__main__":
    print("###---Bitwise Multiplication---###")
    print("%s * %s = %s" % (24, 7, multiply(24, 7)))
