#input: a list of operations for the game. Operations are set, and given defined propblem statement
    #x -> record a score of x, x will be an integer in string form
    #+ -> record a new score, which is the sum of the previous two scores
    #"d" -> record a new score that is 2x the previous score
    #"c" -> remove the previous score from the record

#approach
  #keep track of the scores to be record at the end of the game
  #sequentally apply the operations

  #establish a stack to keep track of the scores
  #establish a dictionary to keep use to reference non-integer opertations

  #iterate over the operations
  #if the operation is integer, add it to the stack
  
  #other wise, access the stored operation in opertions dictionary,
  #apply it to the appropriate values in the stack
    #furthest back value we will need to access in the stack, is 2nd
    #stack.pop, stack.pop -> replace the values as needed.



class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] #use to track scores
        for op in operations:
            if op == "C":
                stack.pop()
                continue
            if op == "D":
                prev = stack.pop()
                new_val = prev*2
                stack.append(prev)
                stack.append(new_val)
                continue
            if op == "+":
                prev = stack.pop()
                second_prev = stack.pop()
                new_val = prev + second_prev
                stack.append(second_prev)
                stack.append(prev)
                stack.append(new_val)
                continue
            try:
                int(op)
                stack.append(int(op))
            except ValueError:
                return None
        
        score = 0
        while len(stack):
            score += stack.pop()

        return score

        