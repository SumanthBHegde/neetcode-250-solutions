class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPr = 0
        slow = 0
        for fast in range(len(prices)):
            pr = prices[fast] - prices[slow] 
            if prices[fast]<prices[slow]:
                slow = fast
            maxPr = max(maxPr,pr)
        return maxPr