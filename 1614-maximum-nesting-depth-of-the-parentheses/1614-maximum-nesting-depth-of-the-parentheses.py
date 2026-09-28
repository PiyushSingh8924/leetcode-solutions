class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxdepth = 0
        depth = 0
        for ch in s:
            if ch == "(":
                depth += 1
                maxdepth = max(depth,maxdepth)
            elif ch == ")":
                depth -= 1
        return maxdepth