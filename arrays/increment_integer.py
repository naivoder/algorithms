"""
this file implements an algorithm to increase an arbitrary precision, nonnegative integer given as an array of digits

the brute force method would be convert the array into an integer, increment, and revert. this could cause overflow in an environment that imposes limits on the range of values an integer can take when the array encodes a value outside of that range.

to solve this problem, mimic the gradeschool addition algorithim, checking for unit overflow only

"""

def increment_int_array(array:list) -> list:
    a = array.copy()
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        # operation is complete
        if a[i] != 10:
            break
        # otherwise, overflow to next 10s place
        a[i] = 0
        a[i - 1] += 1
    # if 10 present at front of array, need another digit to store value
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a

if __name__=="__main__":
    print("###---Increment Arbitrary Precision Integer---###")
    test_numbers = ([1, 2, 3, 4], [8, 9, 9], [9, 9], [5, 3, 5, 7, 9])
    for test in test_numbers:
        print("%s --> %s " % (test, increment_int_array(test)))
