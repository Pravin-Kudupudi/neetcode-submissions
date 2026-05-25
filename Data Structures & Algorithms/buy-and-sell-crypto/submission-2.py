class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - buy)
        
        return ans

