class Solution(object):
    def maxProfit(self, prices):
        so = sorted(prices)
        l = len(so) - 1
        mi = so[0]
        min_ind = prices.index(mi)
        filt_l = prices[min_ind+1:]
        
        while l > 0:
            max_price = so[l]
            if max_price in filt_l:
                return max_price - mi
            l -= 1
        return 0
