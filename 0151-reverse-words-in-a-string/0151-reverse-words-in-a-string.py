#split the string using the native python split method

#assign l and r pointers to the first and last index
#while the l is less/equal to the r, swap the elements, increment l and decrement r

#reform the now reversed list into a string + return it

#this solution will be O(3n) => O(n) time and O(n) space, as the extra array will vary with the worst case being a string of individual characters

class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()
        l,r = 0, len(split_s) - 1

        while l <= r:
            split_s[l], split_s[r] = split_s[r], split_s[l]
            l += 1
            r -= 1

        return " ".join(split_s)    
        