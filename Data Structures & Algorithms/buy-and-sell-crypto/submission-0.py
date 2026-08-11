class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointer
        # left for buy right for sell
        # if left < right check max and move right forward
        # if right <= left set l = r - new low price
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                maxProfit = max(curr, maxProfit)
            else:
                l = r
            r += 1
        
        return maxProfit