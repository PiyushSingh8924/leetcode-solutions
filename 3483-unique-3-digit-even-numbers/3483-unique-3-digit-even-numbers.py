class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
            
        res = 0
        for i in range(100, 1000, 2):
            d1 = i // 100
            d2 = (i // 10) % 10
            d3 = i % 10
            
            freq[d1] -= 1
            freq[d2] -= 1
            freq[d3] -= 1
            
            if freq[d1] >= 0 and freq[d2] >= 0 and freq[d3] >= 0:
                res += 1
                
            freq[d1] += 1
            freq[d2] += 1
            freq[d3] += 1
            
        return res