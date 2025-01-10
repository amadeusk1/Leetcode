
#INCOMPLETTE

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = 999999999999999
        for i in prices:
            if i < low:
                low = i
        high = low
        for i in prices:
            if prices.index(i) > prices.index(low) and i > high:
                high = i
        if high > low: return high - low        
        else: return 0 

        


run = Solution()
print(run.maxProfit([7,1,5,3,6,4]))