class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squ = [x * x for x in nums]
        squ.sort()
        n = len(squ)
        mid = n // 2
        left_half_sum = sum(squ[:mid])
        right_half_sum = sum(squ[mid:])
        return right_half_sum - left_half_sum


