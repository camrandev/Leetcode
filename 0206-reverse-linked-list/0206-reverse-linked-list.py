#move across the linked list, setting the next pointer to the previous node in the list if it exists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #track the current and the previous
        curr = head
        prev = None

        while curr:
            #save the next value
            nxt = curr.next
            #update the next value -> previous value
            curr.next = prev
            #update the previous value to the current value
            prev = curr
            #update the current to the saved next value
            curr = nxt
        
        #return prev, as prev will be pointing to the new head at the end of the algorithm
        return prev
        