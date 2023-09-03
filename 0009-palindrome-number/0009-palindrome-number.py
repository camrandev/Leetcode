class Solution:
    def isPalindrome(self, x: int) -> bool:
        # cast the input x as a string
        # start pointers at index 0, end
        # while left is less/equal to right
        # check if item at left equal item at right
            #if not, return false

        #when the above completes, return true

        s = str(x)
        l = 0
        r = len(s) - 1

        while (l <= r):
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
        
        return True
        