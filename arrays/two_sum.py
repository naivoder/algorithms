"""
this file implements an algorithm to determine if any two integers in an array are equal to a target integer

"""

def two_sum(nums:list, target:int) -> list:
    hash = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash:
            return [hash[diff], i]
        hash[num] = i

if __name__=="__main__":
    print("###---Two Sum---###")
    test_data = [2, 5, 7, 13]; target = 9
    print("Array:", test_data)
    print("Target:", target)
    print("Solution:", two_sum(test_data, target))
