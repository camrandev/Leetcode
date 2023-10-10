# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#starting at the first node of both lists
#access the value of the node, or 0 if it does not exist

#add them together along with the carry if it exists
    #if the value is greater than nine, update the carry variable to equal 1 and the sum to equal 9
    #create a node with the result of the previous operation, and add it to the new list

#return the new list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            s = val1 + val2 + carry

            newv = s % 10
            carry = 1 if s > 9 else 0
            tail.next = ListNode(newv)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        