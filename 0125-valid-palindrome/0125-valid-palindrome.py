class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        n = len(s)
        low = 0
        high = n-1
        while low <= high:
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            elif s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1
        return True