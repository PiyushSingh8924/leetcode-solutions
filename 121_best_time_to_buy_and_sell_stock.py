# 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        maxi = 0
        min_pri = float("inf")

        for i in range(n):
            min_pri = min(min_pri, prices[i])
            maxi = max(maxi, prices[i] - min_pri)

        return maxi
      
# Time: O(n)
# Space: O(1)
