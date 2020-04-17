"""
given a random list of numbers, find the kth smallest number in the list

"""

def kthNumber(k, numbers, debug=False):
    ordered = []
    while numbers:
        min = numbers[0]
        for number in numbers:
            if number < min:
                min = number
        ordered.append(min)
        numbers.remove(min)
        if debug:
            print("Ordered List: ", ordered)
            print("Remaining Numbers: ", numbers)
    return ordered[k-1]

if __name__=="__main__":
    k = 2; numbers = [5, 7, 3, 1, 9, 7, 4]
    answer = kthNumber(k, numbers)
    print("Kth Smallest Number: %d" % (answer))
