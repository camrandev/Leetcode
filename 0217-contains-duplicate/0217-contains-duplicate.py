
#psuedocode

#declare a dictionary to serve as a hash table

#build the hashtable + run the test
#loop over of each num in nums
    #if the num exists in the hashtable as a key -> return true
        #add the number as a key in the hashtable, with a value of one
    
#return false -> does not contain any duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        
        return False
        