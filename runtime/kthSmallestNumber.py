"""
given a random list of numbers, find the kth smallest number in the list

"""

#O(n) solution
def kthNumber_Linear(k, numbers, debug=False):
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

#O(nlogn) solution
def kthNumber_Log(k, numbers, debug=False):
    numbers.sort()
    if debug:
        print("Ordered List: ", numbers)
    return numbers[k-1]


if __name__=="__main__":
    print("O(n) Solution")
    k = 2; numbers = [5, 7, 3, 1, 9, 7, 4]
    answer = kthNumber_Linear(k, numbers)
    print("Kth Smallest Number: %d" % (answer))

    print("\nO(nlog(n)) solution")
    k = 2; numbers = [5, 7, 3, 1, 9, 7, 4]
    answer = kthNumber_Log(k, numbers)
    print("Kth Smallest Number: %d" % (answer))
