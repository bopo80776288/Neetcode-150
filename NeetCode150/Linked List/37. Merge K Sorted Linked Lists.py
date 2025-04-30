# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
from typing import Optional


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(len(lists) - 1):
            lists[i + 1] = self.mergeTwoLists(lists[i], lists[i + 1])
        
        return lists[-1]
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last = dummy 

        while list1 and list2:

            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next

            else:
                last.next = list2
                list2 = list2.next
            
            last = last.next

        last.next = list1 or list2

        return dummy.next