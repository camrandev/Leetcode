# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def _reverse_ll(head):
            """given the head, reverses a linked list in place"""
            curr = head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = _reverse_ll(slow)

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        
        return True
        