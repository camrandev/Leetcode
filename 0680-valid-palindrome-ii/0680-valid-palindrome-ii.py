class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def _isp(p1, p2):
            """determines if a segment of a string is a palindrome from p1 to p2"""
            while p1 <= p2:
                if s[p1] != s[p2]:
                    return False
                p1 += 1
                p2 -= 1
            
            return True
        
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return _isp(l, r-1) or _isp(l + 1, r)
            l += 1
            r -= 1
        
        return True

        