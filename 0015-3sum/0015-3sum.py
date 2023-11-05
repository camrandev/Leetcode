#sort the array
#declare variable to store an output list
#iterate over the array
    #set a pointer, i, to track where we are in the outer loop
    #on each iteration
    #declare pointers l and r
    #declare a sum to be values at i + l + r
    #if the sum is less than 0, increment the l pointer
    #if the sum is greater than 0, break the loop
    #if the sum is equal to 0, add [i, l, r ] to output array

#return the output array once above has finished


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        sorted_nums = sorted(nums)

        for i, num in enumerate(sorted_nums):
            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                s = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    out.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    l += 1
        
        return out

        