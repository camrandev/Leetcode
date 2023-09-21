#need to pick the most profitable trade
#set pointers to buy, sell -> init to 0, 1
#set current max_p, init to 0

#iterate across the length of the array with the sell pointer
#check if the current trade (the current sell price and current buy price) is profitiable
    #if it is, calculate the profit
    #update the max_p tracking variable to the greater of itself and the profit

#if the current trade is not profitiable, we have found a new lowpoint -> move the buy pointer to where the sell pointer is

#move the sell pointer ahead by 1

#return the max profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        maxP = 0


        while s <= len(prices) - 1:
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]
                maxP = max(profit, maxP)
            else:
                b = s
            s+=1
        return maxP
        