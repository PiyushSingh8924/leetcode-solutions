class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n = len(nums1)
        mini = min(nums1)
        if mini % 2 != 0:
            return True
        for num in nums1:
            if num % 2 != 0:
                return False
        return True


        