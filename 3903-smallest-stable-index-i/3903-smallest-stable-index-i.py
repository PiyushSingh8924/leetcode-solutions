class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        min_index = nums[:]
        for i in range(n-2,-1,-1):
            min_index[i] = min(min_index[i],min_index[i+1])
        max_num = nums[0]
        for i in range(n):
            max_num = max(max_num,nums[i])
            if max_num - min_index[i] <= k:
                return i
        return -1