#array index starting at 1

#attempting to find a target value
#only 1 single solution, cannot use an element twice

#start pointers at index 1 and last index

#while l is less than or equal to r
    #calc sum
    #if sum is > target:
        #decrement r
    #if sum is < target:
        #increment l
    #else
        #return integer array of len 2, with indices of elements

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l+1, r+1]        
        