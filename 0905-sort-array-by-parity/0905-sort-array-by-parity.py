#given an array of numbers, with valid data
#return a new array, where all even numbers are first, then all odd numbers
#the order of the digits themselves does not matter, as long as evens and odds are correctly segmented

#create two sub arrays, one with evens, one with odds

#simple merge + return the sub arrays

#O(n) -> because only need one iteration to do the segmentation, and the concation would be O(N) as well, because the complexity scales relative to the combined size of the sub arrays so 2n -> r O(n) time complexity, and a O(1/2N)->n space complexity, because we will have two sub arrays average 1/2 n each, which reduces to N


#how to handle with O(1) extra space and O(n) time complexity
#want evens first, odds second, with no regard for organization within each half

#start pointers at left, right of the array
#if left pointer is on even number, increment it
#if right pointer is on an odd number, decrement it
#if they are both on out of place numbers, swap them

#return the input array

#this would use constant extra
class Solution:
    
    #naive solution
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [num for num in nums if num % 2 == 0]
        odds = [num for num in nums if num % 2 == 1]

        return evens + odds
        
        