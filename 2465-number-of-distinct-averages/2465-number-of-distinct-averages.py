#inputs
#list of numbers, 0 indexed, even length, and a minimum of two values
#values can be between 0 and 100

#while the list still has values, we want to progressively remove + average the largest and smallest value
#calculate the average for that value
#track + return the number of unique averages that appear through the above process

#set pointers to the start and end of the array
#initalize an empty set to hold our averages

#sort the array in non-decreasing order
#using the pointer, which due to the now sorted array, will always sit on the min + max values, we will calculate the average, add that value to the set, and then update the pointers accordingly

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        uniques = set()
        
        l = 0
        r = len(nums_sorted) - 1

        while l < r:
            smallest = nums_sorted[l]
            largest = nums_sorted[r]
            average = (smallest + largest) / 2
            uniques.add(average)
            l += 1
            r -= 1
        
        return len(uniques)
        