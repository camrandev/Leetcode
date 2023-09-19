#move across the two lists in tandem, creating a new list which is the two input lists combineded, sorted in non-ascending order

#use a dummy node to start the list off
#create another variable to track the tail, so we know where to insert

#compare the values at the current nodes in each list, while both lists exist
#add the lesser value to the merged list of list1 and list2 -> list1 and list2 point to a node each
#when an update is performed, update list1/list2 to point to its next property

#if anything remains, add it to the end of the list

#return the merged_list.next value, as merged_list variable will be pointing to the dummy head node. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        tail = merged_list

        #perform the main merge -> dont forget to update the pointers for the list nodes
        while(list1 and list2):
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #update the tail, so we know where to insert

        #merge any remaining poritions
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return merged_list.next #merged_list.next points to the value that we want
        