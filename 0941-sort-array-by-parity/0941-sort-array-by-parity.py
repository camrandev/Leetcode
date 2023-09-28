class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        front = []
        back = []

        for num in nums:
            if num % 2 == 0:
                front.append(num)
            else:
                back.append(num)
        
        return front + back
        