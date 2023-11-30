#summary: return a boolean indicating if a string is a palindrome except for
#one character -> so one mismatch is allowed in the string

#input: is a string
#output: a boolean, indicating if the string satifies the condition above

#helper method -> checks if a segment of a string from start to end is a palindrome
#inputs: string, starting index, ending index
#output: boolean, indicating if string from start to end index is palindromic

#use two pointer approach, with start and end as pointers
    #move the pointers towards eachother, checking if corresponding characters are
    #the same
        #if not, return false
    #update the pointers

    #if the pointers reach eachother wihtout a return, return true

#main method
    #two pointers again
    #set left, right pointer, left starts at 0, right starts at end
    #move them towards eachother
        #if characters at pointers do not match
        #call helper on segment created by skipping each pointer, and return
        #the results of those calls
        #call it passing in l + 1, r and l, r - 1
    #update our pointers

    #if process abovce completes without a return, we return true

#uses O(n) time and constant space, as only storage is the pointers and the number
#of calls to the hlper method does not scale with the length of the input.

#a recursive solution would be O(n) space, as the number of calls would scale directly with the input length
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def _ispal(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start, end = start + 1, end - 1
            
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return _ispal(s, left + 1, right) or _ispal(s, left, right- 1)
            left, right = left + 1, right - 1
        
        return True

            
        