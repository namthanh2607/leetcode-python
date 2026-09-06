# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        cut_ind = dummy
        count = 0 
        while cur:
            if count >= n + 1:
                cut_ind = cut_ind.next
            cur = cur.next
            count += 1
        if cut_ind.next == None:
            cut_ind.next = None
        else:
            cut_ind.next = cut_ind.next.next
        return dummy.next  