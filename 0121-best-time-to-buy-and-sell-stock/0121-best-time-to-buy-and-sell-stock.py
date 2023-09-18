#overview: find the most profitable potential stock trade. At a very high level, we need to move acorss the array, finding the lowest values, and finding the highest value after that, if we find a value lower than the current low, set the low to the new low


#approach - this works because the tracked profit tracks the actual max profit, pointers only care if an individual trade is profitable
#set pointers to b and s
#set current max profit to 0

#want to move the sell point all the way across the list, the buy point will be updated as apprpriate

#check if a current trade is a profitable one
#it is profitable if the value at s is greater than the value at b
    #if it is a profitable trade, then check if it is more profitable than current max and update accordingly

#if not a profitable trade
    #move b pointer to the current position of the sell pointer, as it indicates we have found a new low point

#update the b pointer one space

#return the profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        max_p = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                max_p = max(max_p, profit)
            else:
                b = s
            s += 1
        
        return max_p
        