
#input: a string of of parenthetical characters
#output: a boolean, indicating if the string contains only valid pairs

#we know that we will only receive valid data, and do not have to account for characters that do not fit the pattern

#approach
#create a stack to keep track of the opening paranthesis 
#create a dictionary maping closing characters to opening characters

#iterate over string

#if a character is not in the map, add it to the stack & continue

#otherwise
    #check if the value stored in the map at the current character is equal to the top value of the stack (this would indicate a valid pair was found)
        #if so, pop the top value off the stack
        #if not, immediately return false

#if the above operation has completed and the stack is empty, then return true otherwise, return false




class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char in pairs and stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if stack:
            return False
        
        return True

                
