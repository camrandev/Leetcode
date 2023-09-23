

#determine if palindrome
#set pointers to start, end of of cleaned string
#work our way towards the middle, accounting for a string of uneven length, checking if the characters are the same, if they are not the same
    #early return false

#return true

#aaa

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #strip + format the string
        s_clean = "".join(char.lower() for char in s if char.isalnum())

        #determine if palindrone
        l = 0
        r = len(s_clean) - 1

        while l <= r:
            if s_clean[l] != s_clean[r]:
                return False
            l +=1
            r -=1
        
        return True



        
        