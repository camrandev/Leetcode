class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #declare pointers to track search range, remember to declare left first
        l, r = 0, len(nums) - 1


        while (l <= r):
            m = (l + r) // 2
            if target > nums[m]:
                #move l forward to one position ahead of m
                l = m + 1
            elif target < nums[m]:
                #move r backward to one position after m
                r = m - 1
            else:
                return m
        return -1
        