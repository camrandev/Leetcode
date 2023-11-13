#given list of string, find first string that is palindromic (same from first to last)
#we know that strings will be at least 1 character long
#and we know that strings will only consist of lowercase english letter

#create a helper method to check if a string is palindromic
#iterate over the input list, checking each word, if it is a palindrome, return the word

#if the above completes with a return return an empty string

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def _is_palindrome(s: str) -> bool:
            l,r = 0, len(s) - 1
            
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        for word in words:
            if _is_palindrome(word):
                return word
        
        return ""
        