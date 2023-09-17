#use a hashmap to implement a frequency table

#iterate over the array
    #update the current values freqency
    #check the frequency against the target, if true return the element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = {}
        len_div_2 = len(nums) / 2

        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1
            if count_nums[num] > len_div_2:
                return num
    
        