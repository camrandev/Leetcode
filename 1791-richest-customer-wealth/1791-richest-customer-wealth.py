#use variable to track the current max wealth

#iterate over the array of sub arrays
    #sum each sub array
    #set the tracking variable to the max of the sum and the currext max

#return the max after all operations complete
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxw = 0

        for acc in accounts:
            wealth = sum(acc)
            maxw = max(wealth, maxw)
        
        return maxw
        