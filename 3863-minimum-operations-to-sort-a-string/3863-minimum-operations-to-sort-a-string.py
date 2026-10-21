class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        if all(s[i] <= s[i+1] for i in range(len(s) - 1)):
            return 0
        if len(s) == 2:
            return -1
        mn = min(s)
        mx = max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if s.find(mn) == len(s) - 1 and s.rfind(mx) == 0:
            return 3
        return 2