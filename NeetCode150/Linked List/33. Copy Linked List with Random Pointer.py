"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = { None:None }

        cur = head
        while cur:
            # create a node that is a copy of cur.val ex. Node(3)
            copy = Node(cur.val)
            # assign [cur:copy] ex. [[3,null]:Node(3)]
            old_to_copy[cur] = copy 
            cur = cur.next
        
        cur = head
        while cur:
            # call out the copy node 
            copy = old_to_copy[cur]
            # assign copy.next by using the hash map 
            # cur.next will bring us the [val:random] pair key that will map to a copy node
            copy.next = old_to_copy[cur.next]
            # assign copy.random by using the hash map 
            copy.random = old_to_copy[cur.random]
            cur = cur.next
        
        return old_to_copy[head]

        

            

        

            