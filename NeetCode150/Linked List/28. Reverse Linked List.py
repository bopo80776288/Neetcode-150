from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        # set the given head node = current, previous = None 
        while current:
            # make temp = current.next to keep the value before we assign current.next = previous 
            # so tha we don't lose the value
            #   0 1 2 3 4 5 
            # p c t 
            # think of it as we are moving the p c t towards right and build the link from 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None
            temp = current.next 
            current.next = previous 
            previous = current
            # when moving use = when assigning use .next
            current = temp 
        
        return previous 

# Helper function to convert a list to a linked list
def list_to_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

# Create a linked list from the given list
head = list_to_linked_list([0, 1, 2, 3])

solution = Solution()
reversed_head = solution.reverseList(head)

# Print the reversed linked list
print_linked_list(reversed_head)

