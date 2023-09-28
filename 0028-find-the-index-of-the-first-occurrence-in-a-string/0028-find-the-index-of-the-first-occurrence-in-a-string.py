#Approach

#iterate over the haystack
#as we go, check if the current element plus the next n elements, with n being length of need - 1 is equal to the needle
#if it is, return the index of the current element

#return -1


#psuedo
#save window size as the length of the needl - 1

#iterate over the list
#check if the window the saize of window size, starting at current index is equal to need
#if it is, return the current elements index

#return -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        window = len(needle)
        

        for index, char in enumerate(haystack):
            if haystack[index:(index + window)] == needle:
                return index

        return -1
        