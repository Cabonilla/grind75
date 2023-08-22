# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slw,fst = head, head

        while fst and fst.next:
            slw = slw.next
            fst = fst.next.next

        return slw