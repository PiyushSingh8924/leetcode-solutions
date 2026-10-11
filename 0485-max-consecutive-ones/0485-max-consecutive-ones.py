class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                max_count = max(right-left+1,max_count)
            else:
                left = right + 1
        return max_count