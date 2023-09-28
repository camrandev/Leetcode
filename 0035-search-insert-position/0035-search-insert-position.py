#run a binary search on nums, at the end, either return the index of midpoint if the midpoint is equal to the target, and return the index +1 or -1 if index is greater/less than target




class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums) - 1

        while (l <= r):
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return l

            
        