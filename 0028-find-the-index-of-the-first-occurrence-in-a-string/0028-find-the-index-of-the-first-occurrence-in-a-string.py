class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        window = len(needle)

        while p1 <= len(haystack) - window:
            if haystack[p1:p1 + window] == needle:
                return p1
            else:
                p1 +=1

        return -1
        