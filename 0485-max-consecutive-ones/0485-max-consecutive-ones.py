class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        curr_count = 0
        for num in nums:
            if num == 1:
                curr_count += 1
                max_count = max(curr_count,max_count)
            else:
                curr_count = 0
        return max_count