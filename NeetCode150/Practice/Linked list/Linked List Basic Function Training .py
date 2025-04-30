# A linked list is a linear data structure that contains data (value) and a reference (link) to the next node n the list 
# Each node points to the next node, and the last node points to None, indicating the end of the list.

# We define a class ListNode. This class represents each node in the linked list.
# A class in Python is a blueprint for creating objects. 
# Here, the ListNode class will serve as a blueprint for creating individual nodes in our linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

## Create a linked list
def create_linked_list(values):
    if not values:  # Check if the list is empty
        return None

    # Create the head node
    head = ListNode(values[0])
    current = head

    # Create the rest of the nodes
    for val in values[1:]:
        current.next = ListNode(val)  # Create the next node
        current = current.next  # Move to the next node

    return head  # Return the head of the linked list

# Example usage
values = [1, 2, 3]
head = create_linked_list(values)

# Output the list
current = head
while current:
    print(current.val, end="->")
    current = current.next
print("None")

### Practice Questions:
## Write a function to add a node at the beginning of the linked list.
def add_node_at_beginning(head, value):
    new_node = ListNode(value)
    new_node.next = head
    return new_node

# Example usage
values = [1, 2, 3, 8, 9, 71]
head = create_linked_list(values)
updated_head = add_node_at_beginning(head, 5)

# Output the list
current = head
while current:
    print(current.val, end="->")
    current = current.next
print("None")

## Write a function to add a node at the end of the linked list.
def add_node_at_end(head, value):
    new_node = ListNode(value)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Example usage
values = [1, 2, 3, 9, 71, 102]
head = create_linked_list(values)
updated_head = add_node_at_end(head, 6)

# Output the list
current = head
while current:
    print(current.val, end="->")
    current = current.next
print("None")

## Write a function to delete a node by value (remove the first occurrence of a node with a specific value).
def delete_node_by_value(head, value):
    # If the list is empty
    if not head:
        return None
    
    # Handle the case where the head needs to be deleted
    if head.val == value:
        return head.next  # Just return the next node as the new head
    
    current = head
    previous = None
    while current:
        if current.val == value:
            previous.next = current.next
            return head
        previous = current
        current = current.next
    return head

# Example usage
values = [1, 2, 3, 9, 71, 102]
head = create_linked_list(values)
updated_head = delete_node_by_value(head, 3)

# Output the list
current = head
while current:
    print(current.val, end="->")
    current = current.next
print("None")

## Write a function to reverse the linked list in place.
def reverse_linked_list(head):
    if not head:
        return None
    current = head
    previous = None

    while current:
        right = current.next
        current.next = previous 
        previous = current 
        current = right
    
    return previous 

# Example usage
values = [1, 2, 3, 9, 71, 102]
head = create_linked_list(values)
reversed_head = reverse_linked_list(head)

# Output the list
current = reversed_head
while current:
    print(current.val, end="->")
    current = current.next
print("None")
