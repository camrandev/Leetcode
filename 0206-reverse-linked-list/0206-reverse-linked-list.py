# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #track curr, prev
        curr, prev = head, None

        while curr:
            #save next
            nxt = curr.next
            #set next
            curr.next = prev
            #update pointers (curr->nxt, prev->curr)
            curr, prev = nxt, curr
        
        #prev -> because previous will now be pointing to the new head
        return prev
        