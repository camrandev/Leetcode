class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        input_set = set(nums)

        for i in range(0, len(nums)+1):
            if i not in input_set:
                return i
        