class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sumd = 0
        prod = 1
        num = n
        while num > 0:
            digit = num % 10
            sumd += digit
            prod *= digit
            num = num // 10
        return (n % (sumd + prod)) == 0