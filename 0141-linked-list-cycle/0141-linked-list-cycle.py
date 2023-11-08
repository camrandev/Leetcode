# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#we are looking for either a node with a null next pointer, indicating a none cycle, OR a point where the two nodes are equal, indicating a point where a cycle has occured

#floyds detection algo - fast/slow pointers, 2:1 ratio

#declare fast and slow pointers, start them both at the head

#while the fast pointer has a next value -> indicating that we are not at the end of the list
    #increment the slow pointer by one
    #increment the fast pointer by two
    #if the fast and slow are equal, return true, indicating a cycle

#if this code is reached, it means we have hit a cycle, and thus return false




class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False

        