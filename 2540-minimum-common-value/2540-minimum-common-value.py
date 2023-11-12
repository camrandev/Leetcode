
#pointer approach
#start two pointers from the wfront of both lists, icnrement them until we either find a match or run into the end of the shorest list, but need to account for both
#becuase the lists can have different length
#set our pointers to 0 and 0
#run a loop while their are elements in either list
#if current l1 value is less than l2 value, increment it and continue
#if current l2 value is less than l1 value, increment it and continue
#if equal, return the value itself

#if above completes without a return, then return negative one

#TC -> O(n), contstant space complexity

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
                continue
            if nums2[p2] < nums1[p1]:
                p2 += 1
                continue
            if nums2[p2] == nums1[p1]:
                return nums1[p1]
        
        return -1
            

        