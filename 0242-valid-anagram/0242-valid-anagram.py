
#create a frequency table for each string
#check if the frequency tables are the same by value, can do python using ==, in javascript it would require manual iteration over the strings



class Solution:
    def map_s(self, s:str)->dict:
        out = {}
        for char in s:
            out[char] = out.get(char, 0) + 1
        
        return out

    def isAnagram(self, s: str, t: str) -> bool:
        s_table = self.map_s(s)
        t_table = self.map_s(t)

        return s_table == t_table
        
        
        