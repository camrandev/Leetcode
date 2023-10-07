# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#set 2 pointers
#start them both at the head
    #increment first pointer by 1 node per cycle, second pointer by 2 nodes per cycle
    #second pointer will finish 2x as fast, when it finishes, first pointer will be in the middle

    #return the first pointer

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head

        #run the iteration while there are at least 2 nodes left
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        return p1