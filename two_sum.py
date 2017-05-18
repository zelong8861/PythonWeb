class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, index in enumerate(nums):
            other = target - index
            try:
                position = nums.index(other)
                if (position != i):
                   return sorted([i, position])
            except ValueError:
                pass