
#copy nums by value
#create new array, ans

#contacts copy to ans 2x

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = nums[:]

        return nums + copy

        