#set pointers to track the buy and sell price
#set variable to track the current max profit

#move the pointers across prices to deterimine the max price

#price determination algo:
#with b starting at 0 and s starting at 1
    #check if s is greater than b
        #if it is, calculcate the profit of buying at b and selling at s
        #if that profit is greater than the current max, update it
    #if s is not greater than b, you have found a dip
        #move b over to where s is
    #move s ahead by 1
        #this works, because anytime b pointer is > s pointer, you have found a potential buy point, and the algorithm will then check the profit for each possible trade after this against the current max profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        max_p = 0

        while (s < len(prices)):
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]
                max_p = max(profit, max_p)
            else:
                b = s
            s += 1

        return max_p        