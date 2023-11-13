#given two strings, s and t -> return true of S is a sub sequence of T, return  false otherwise
#input: two strings of varrying lengths, can be empty
#output: boolean indicating if the first string is a sub sequence of the second string

#set pointers to track our position in s and t, init both to 0

#loop condition: -> only want to run the looping while both elements have anything left,
#becuase if we reach either condition, we are done 
    #as long as the s pointer is less than or equal to number of elements in s
    #as long as the t pointer is less than the number of elements in S

    #if the value at the t pointer is == to the value at the s pointer
        #increment both pointers
        #if s pointer has become greater than the length s, that is our success condition -> return True

    
    #increment the t pointer

    #return
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        ps = pt = 0

        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                if ps >= len(s):
                    return True            
            pt += 1
        
        return False

#complexity:
    #this problem has O(n) time, where N is the combined length of the input arrays, and constant space as the only thing getting stored are the pointers
        