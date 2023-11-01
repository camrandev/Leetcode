#psuedocode
#declare a map to store which numbers have been looked at

#iterate over the nums
    #calculate the complement - the value that which added to the current num = the target
    #if the comp exists in the map
        #return the index of the comp + the current index
    #otherwise
        #add the comp to the map as a key, storing its index as a value
    
    #nothing else is required, as we know we will always have a working solution according to the prompt


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        #iterate over the numbers, accessing both the index and number
        for i, num in enumerate(nums):
            #calculate the complement
            comp = target - num
            #check if the complement exists in the hash
            if comp in hash:
                #if it does, return the value at the complement in the [hash, index]
                return [hash[comp], i]
            else:
                #if comp not in hm: add the current number as a key, with index as value
                hash[num] = i

        