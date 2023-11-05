#set three pointers, red, white, blue
#init red/white to first index, blue to last index

#create a loop over nums
    #if white is on a 0:
        #swap values at red, white
        #increment them both
    #if white is on a 1:
        #increment it
    #if white is on 2:
        #swap values
        #decrement blue
   

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1

