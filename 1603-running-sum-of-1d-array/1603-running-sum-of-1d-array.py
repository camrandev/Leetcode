#iterate across the list, and for each value set it equal to itself + the sum of ever previous element
#need to track the some

#set a variable to store the "prev" value, initialize it to 0
#set a variable to store the output array

#starting at the first value in input
    #append current element + running sum to the output array

#return the output array

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 0
        out = []

        for num in nums:
            new = num + prev
            prev = new
            out.append(new)
        
        return out