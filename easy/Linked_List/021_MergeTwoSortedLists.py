from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        cur_node = ret

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                cur_node.next = list1
                cur_node = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                cur_node = list2
                list2 = list2.next

        if list1 == None:
            cur_node.next = list2
        if list2 == None:
            cur_node.next = list1

        return ret.next
            

            


