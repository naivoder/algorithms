"""
this file implements an algorithm that computes a running sum of a given 1D array

"""

class Solution:
    def running_sum(self, nums:list) -> list:
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i-1]
        return nums

if __name__=="__main__":
    test_data = [1, 5, 2, 6, 7, 4]
    print("###---Compute Running Sum---###")
    result = Solution()
    print("Test array:", test_data)
    print("Solution:", result.running_sum(test_data))
