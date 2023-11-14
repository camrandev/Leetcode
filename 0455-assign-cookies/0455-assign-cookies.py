#s is the list of cookies, denoted by size, can be empty
#g is the list of children, denoted by greed factor, will always have at least one value
#cookie can only be assigned to a child, if cookie >= child

#JUST trying to maximize the number of content children
#each cookie can only be asigned one time

# Set two pointers starting at the start of both arrays
# contraints appear to indicate that the arrays are sorted,

#conditions for moving the pointers
    #if s is less than g, increment s, leave g
    #otherwise
        #increment counter, update both pointers



class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_sorted = sorted(g)
        s_sorted = sorted(s)
        p1 = 0
        p2 = 0
        num_happy = 0

        while p1 < len(g) and p2 < len(s):
            if s_sorted[p2] < g_sorted[p1]:
                p2 += 1
                continue
            num_happy += 1
            p1 += 1
            p2 += 1
        
        return num_happy
        