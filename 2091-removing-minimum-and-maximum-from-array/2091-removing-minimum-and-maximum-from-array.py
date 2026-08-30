class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        i = min(min_index,max_index)
        j = max(min_index,max_index)

        front = j + 1
        back = n - i
        both = (i+1) + (n - j)

        return min(front,back,both)