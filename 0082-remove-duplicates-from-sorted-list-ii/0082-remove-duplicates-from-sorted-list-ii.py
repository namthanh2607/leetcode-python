# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                val_to_remove = prev.next.val
                while prev.next and prev.next.val == val_to_remove:
                    prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
