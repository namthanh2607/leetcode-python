# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode(0)

class Solution:
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = a
           
        return dummy.next