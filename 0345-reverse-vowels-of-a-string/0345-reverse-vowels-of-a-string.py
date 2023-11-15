#create a structure to hold the vowels as a reference -> use a set, because of constant look up time

#set pointers to start and end of s, and move them towards eachother
#move r pointer until it hits a vowel
#move l pointer until it hits a vowel
#swap them, and move both pointers

#return s, which has been modified in place

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        s_list = list(s)

        l,r = 0, len(s_list) - 1

        while l <= r:
            if not s_list[l].lower() in vowels:
                l += 1
                continue
            if not s_list[r].lower() in vowels:
                r -= 1
                continue
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        
        return "".join(s_list)
        