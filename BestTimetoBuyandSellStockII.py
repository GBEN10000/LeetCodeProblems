class Solution(object):
    def maxProfit(self, prices):
        l = len(prices)
        result = 0
        for i in range(0, l - 1):
            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]
                print(result)
        return result


