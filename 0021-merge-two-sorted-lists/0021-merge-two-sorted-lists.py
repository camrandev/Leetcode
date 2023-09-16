# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#track the new list
#perform the main merge
#add any remianing to the end of the new list
#return the head node of the new list

#psuedocode

#setup problem
#declare a variable to hold a dummy node
#keep track of the tail, so we know where to add any values

#main merge
#while both lists exist
    #if val of list1 > the value of list2
        #set the tails next to the list 2 node
        #set the list2 pointer to its next value    
    #else:
        #set the tails next pointer to the list1 node
        #set the list 1 pointer to its next value
    #set the tail to its own next pointer

#merge any remianing values
    #don need to track the tail after this step
    #if list1 exists -> set the tails next to l1
    #set tails next to list2

#return the merged list

# list1 = [1,2,4], list2 = [1,3,4]        

#l1 = 2
#l2 = 1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        tail = merged_list # 1 2*

        #do the main merge while we have two lists
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        #merge the remaining
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        #must return merged_list.next, as merged_list itself is a dummy node
        return merged_list.next
        

        