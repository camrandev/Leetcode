# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#determine the size of the list -> 1 iteration
#iterate up to the size / 2 rounded up node
#return it

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        mid = size // 2
        count = 0
        
        while head:
            if count == mid:
                return head
            else:
                count += 1
                head = head.next
        
        return head
            
        