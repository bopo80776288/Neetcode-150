# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length of the linked list
        lenght_of_list = 0
        current = head
        while current:
            current = current.next
            lenght_of_list += 1 
        
        # Compute the index to removed 
        index_to_be_removed = lenght_of_list - n 
        
        # Edge case: If we need to remove the head
        if index_to_be_removed == 0:
            return head.next
        
        # Initialize pointers for traversal
        current_index = 0
        current = head
        previous = None

        while current:
            # after we skip the index we can just skip
            if current_index == index_to_be_removed:
                previous.next = current.next
                break
            
            previous = current 
            current = current.next
            current_index += 1 
            
        return head

