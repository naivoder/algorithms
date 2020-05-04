"""
this file implements a recursive solution to find the factorial of a given number

"""

def factorial(number=None):
    result = 1
    if number is None:
        number = int(input("Please enter a number: "))
    if number == 1:
        return result
    return factorial(number - 1) * number

if __name__=="__main__":
    solution = factorial(5)
    print(solution)
