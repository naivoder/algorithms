"""
this file implements an algorith that shuffles by interweaving a given array

eg: [2, 1, 4, 5, 3, 8] --> [2, 5, 1, 3, 4, 8]

"""

class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        new = nums.copy()
        for i in reversed(range(n)):
            move = new.pop(i)
            new.insert(i+i, move)
            i -= 1
        return new

if __name__=="__main__":
    test_data1 = [0, 1, 6, 1, 9, 8]
    test_data2 = [2, 5, 1, 3, 4, 7]
    print("###---Shuffle Array---###")
    solution = Solution()
    print(test_data1, '->', solution.shuffle(test_data1, 3))
    print(test_data2, '->', solution.shuffle(test_data2, 3))
