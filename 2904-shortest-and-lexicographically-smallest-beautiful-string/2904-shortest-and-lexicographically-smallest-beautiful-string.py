class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        count = 0
        ans = ""
        
        for right in range(len(s)):
            if s[right] == '1':
                count += 1
            while count > k or (count == k and s[left] == '0'):
                if s[left] == '1':
                    count -= 1
                left += 1
            if count == k:
                curr = s[left:right+1]
                if not ans or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                    ans = curr               
        return ans