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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2
        dummy = ListNode()  # Dummy node to simplify result handling
        last = dummy  # This keeps track of the last node in the result list
        carry = 0  # Carry to handle sums greater than 9
        
        while cur1 or cur2 or carry:  # Continue until both lists are exhausted
            val1 = cur1.val if cur1 else 0  # If cur1 is None, treat its value as 0
            val2 = cur2.val if cur2 else 0  # If cur2 is None, treat its value as 0
            
            total = val1 + val2 + carry  # Add the values and the carry from previous iteration
            carry = total // 10  # Calculate the new carry for the next iteration
            temp = ListNode(total % 10)  # Create a new node for the current digit
            last.next = temp  # Link the node to the result list
            last = last.next  # Move the last pointer to the new node
            
            # Move cur1 and cur2 to their next nodes, if they exist
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        return dummy.next  # Return the result list starting from the first real node (dummy.next)

        