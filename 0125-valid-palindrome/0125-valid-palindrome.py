#strip the string + convert into lower cast
#set pointers to the start and the end
#while the left is less/equal to the right
    #check if the values at the pointers are equal
    #if not, return false

    #return true



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = "".join(char.lower() for char in s if char.isalnum())
        p1, p2 = 0, len(s_alnum)-1
        print(s_alnum)

        while (p1 <= p2):
            if s_alnum[p1] != s_alnum[p2]:
                return False
            p1+=1
            p2-=1
        
        return True

    
        
        