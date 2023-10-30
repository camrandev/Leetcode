#check if a string is the same front to back

#format the string: all lowercase, remove all non-alphanumeric characters

#set pointers to front and end

#check if the values at the pointers are the same

#if they are not, return false
#repeat process for all of the characters

#if the process above is able to complete, we have a palindrome and we return
#true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(char.lower() for char in s if char.isalnum())

        l = 0
        r = len(stripped) - 1

        while l < r:
            if stripped[l] != stripped[r]:
                return False
            r -= 1
            l += 1
        
        return True
        