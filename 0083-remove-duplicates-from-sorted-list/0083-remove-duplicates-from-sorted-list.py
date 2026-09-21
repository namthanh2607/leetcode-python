# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = head
        cur = dummy
        while cur:
            if cur.next and cur.next.val == cur.val:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            else:
                cur = cur.next
        return dummy