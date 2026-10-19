class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digit = False
        expo = False
        dot = False
        for i , ch in enumerate(s):
            if ch.isdigit():
                digit = True
            elif ch in ["+","-"]:
                if i > 0 and s[i-1] not in ["e","E"]:
                    return False
            elif ch in ["e", "E"]:
                if expo or not digit:
                    return False
                expo = True
                digit = False
            elif ch == ".":
                if dot or expo:
                    return False
                dot = True
            else:
                return False
        return digit


