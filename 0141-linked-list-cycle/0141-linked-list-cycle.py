# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#inputs: a linked list, that may or may not contain a cycle
#output: a boolean, indicating if a cycle is present in our linked list

#contraints
#test cases

#declare two pointers, fast and slow, initiate them to the head of the list

#declare the main loop to run while we have a fast pointer and a fast.next pointer
    #increment the slow pointer 1 node
    #increment the fast pointer 2 nodes
    #check if they are on the same node
        #if so, return True -> as we have found a cycle
    
    #if the process above completes -> it means that we have hit the end 
    #of the list, so we return false

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #need to use is, to check if they are on the same memory reference         
            if slow is fast:
                return True
                
        return False

        