#take the last k elements, move them to the front of the array

#bruteforce
#iterate up to k
    #on each iteration
    #save + pop the last value
    #insert it at the front

#optimal

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #bruteforce
        index = 0
        while index < k:
            val = nums.pop()
            nums.insert(0, val)
            index+=1
        #optimal
        