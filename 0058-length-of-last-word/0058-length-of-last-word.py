#split the string into a list of words
#python split method takes care of the trimming for us
#return the length of the last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])