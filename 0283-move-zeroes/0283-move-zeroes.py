class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0  # Pointer to the current position to place a non-zero element
        # Iterate through the array
        for r in range(len(nums)):
            if nums[r] != 0:
                # Swap the non-zero element to the 'l' position
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  # Move the 'l' pointer to the next position