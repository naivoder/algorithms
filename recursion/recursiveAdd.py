"""
this file implements basic addition as a recursive funtion

"""

# non-recursive solution
def calcSum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# recursive solution
def add(numbers=None):
    if numbers is None:
        numbers = getNumbers()
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add(numbers[1:])

def getNumbers():
    numberList = []
    equation = input("What addition problem should we solve? ")
    for char in equation:
        if char.isdigit():
            numberList.append(int(char))
    return numberList

if __name__=="__main__":

    numberList = [1, 2, 5, 3, 2, 7, 4, 3, 7, 9, 8, 5, 4, 2, 3, 1]

    print("Non-recursive solution:", calcSum(numberList))
    print("Recursive solution:", add(numberList))
    print("Recursive solution:", add())
