#input: an array of numbers
#output: two values:
    #K:Int, a count of the number of elements in the original array which are NOT equal to val
    #nums: the original array, starting with all of the non-val elements.

#Psuedocode
#create a variable to track the count of non-val nums, set it 0
#loop over the input array
    #need to be aware of potential for an infinite loop here

#for each element of the array:
    #check if the current element is equal to the target
    #if is
        #increment our count
        #store the index in a seperate list
    
    #iterate over our list of indices
    #for each index, pop the value from the input list, and append to the end of the input list

    #return the count and the modified nums list


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)


    
        