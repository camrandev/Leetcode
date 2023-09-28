#init a varaible to track the max

#iterate across the main array
#sum each sub array
#check if the sum is greater than the tracked max outside of the loop

#return the tracked max

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxw = 0

        for acc in accounts:
            value = sum(acc)
            maxw = max(value, maxw)
        
        return maxw
        