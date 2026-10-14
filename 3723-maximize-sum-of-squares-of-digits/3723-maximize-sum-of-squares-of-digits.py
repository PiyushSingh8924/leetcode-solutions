class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > num * 9:
            return ""
        nines = sum // 9
        remainder = sum % 9
        if nines == num:
            return "9" * num
        return "9" * nines + str(remainder) + "0" * (num - nines - 1)