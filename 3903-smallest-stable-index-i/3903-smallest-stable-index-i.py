class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            max_num = nums[0]
            for j in range(i + 1):
                max_num = max(max_num, nums[j])
            min_num = nums[i]
            for j in range(i, n):
                min_num = min(min_num, nums[j])
            if max_num - min_num <= k:
                return i
        return -1