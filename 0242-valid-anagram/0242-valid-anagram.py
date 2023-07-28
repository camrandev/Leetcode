class Solution:
    def generateFreqTable(self, s: str):
        table = {}
        for char in s:
            table[char] = table.get(char, 0) + 1 
        return table


    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): 
            return False

        s_table = self.generateFreqTable(s)
        t_table = self.generateFreqTable(t)

        if s_table != t_table:
            return False

        return True