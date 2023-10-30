#track the current max profit, initialize to 0
#set pointers to b and s, starting them at 0 and 1

#check if the current trade b - s, is profitable
    #if it is, set the max profit tracker to the greater of itself and the current
    #trades profit
    #if if not, you have found a vallue
        #move the buy to the sell
    #increment the sell

    #repeat the above process until sell pointer has reached the end of the list

    #return the max profit tracking variable

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        b,s = 0, 1

        while s <= len(prices) - 1:
            if prices[s] - prices[b] > 0:
                profit = prices[s] - prices[b]
                maxp = max(maxp, profit)
            else:
                b = s
            s += 1
        
        return maxp
        