# Definition for singly-linked list.
from types import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def twoList(l1, l2):
            curr = dummy = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2

            return dummy.next

        lls = len(lists)
        if lls == 0:
            return None
        elif lls == 1:
            return lists[0]

        currl = lists[0]
        for l in range(1, lls):
            currl = twoList(currl, lists[l])
        return currl