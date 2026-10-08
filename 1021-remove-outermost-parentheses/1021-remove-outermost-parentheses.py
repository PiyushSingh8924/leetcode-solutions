class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opened = 0
        for c in s:
            if c == '(':
                if opened > 0:
                    res.append(c)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    res.append(c)
        return "".join(res)