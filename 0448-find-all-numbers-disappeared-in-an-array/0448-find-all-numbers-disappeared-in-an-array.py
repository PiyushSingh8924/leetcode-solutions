class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        missing_numbers = []
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                missing_numbers.append(i)
        return missing_numbers
        