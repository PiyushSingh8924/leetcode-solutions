class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = 0
        for ch in s:
            if ch == '(':
                count += 1
            if ch == ')':
                if count > 0:
                    count -= 1
                else:
                    n += 1
        return count + n