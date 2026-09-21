# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution():
    def rotateRight(self, head, k):
        dummy = head
        cur = dummy
        count = 0
        while cur:
            count = count + 1
            final = cur
            cur = cur.next

        if count in [0,1] or k == 0:
            return dummy

        cur = dummy
        count_rotate = count - k % count
        if count_rotate == count:
            return dummy
        count = 0
        if count_rotate == 0:
            return dummy
        else:
            while cur:
                count = count + 1
                if count == count_rotate:
                    dummy = cur.next
                    final.next = head
                    cur.next = None
                cur = cur.next
        return dummy
        