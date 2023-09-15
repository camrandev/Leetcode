class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key in hashmap:
            if hashmap[key] == 1:
                return key
        

        