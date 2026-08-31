class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mis = 1
        for num in nums:
            if num == mis:
                mis += 1
            elif num > mis:
                return mis
        return mis