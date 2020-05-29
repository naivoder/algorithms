"""
this file implements an algorithm to compute x**y using bitwise operations
this is another conceptually challenging algorithm taken from EPI

the brute force approach is of course to start with 'x' and multiply it by 'x' 'y' number of times
this results in O(2^n) runtime where n = number of bits to represent 'y'

a more efficient solution comes from the idea that (X^10) = (X^(5+5)) = (X^5) x (X^5)
in binary: x^(1010) = x^(101) * x^(101) --> x^(101) = x^(100) * x^(001)

generally speaking, if the lsb of y = 0, the computation is (x^(y/2))^2
otherwise the computation is x*(x^(y/2))^2
if y is negative, replace x by 1/x and y by -y

this algorithm has at most twice the number of multiplications as the index of y's MSB
implying a time complexity of O(2n) == O(n)

"""
import random

def power(x:int, y:int) -> int:
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1/x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

def recursive_power(x:int, y:int, result=None) -> int:
    if result == None:
        result = 1.0
    power = y
    if y < 0:
        power, x = -power, 1/x
    if power <= 1:
        return result * x
    if power & 1:
        return recursive_power(x * x, power >> 1, result * x)
    return recursive_power(x * x, power >> 1, result)

if __name__=="__main__":
    print("Using while loop:")
    x_data = [random.randint(1,10) for num in range(10)]
    y_data = [random.randint(-10, 10) for num in range(10)]
    for i in range(len(x_data)):
        result = power(x_data[i], y_data[i])
        print("%3s raised to the %3s power = %22.8f" % (x_data[i], y_data[i], result))
    print("Using recursive function:")
    x_data = [random.randint(1,10) for num in range(10)]
    y_data = [random.randint(-10, 10) for num in range(10)]
    for i in range(len(x_data)):
        result = recursive_power(x_data[i], y_data[i])
        print("%3s raised to the %3s power = %22.8f" % (x_data[i], y_data[i], result))
