# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        len = 0

        l = head
        while l:
            len += 1
            l = l.next
        print(len)

        dl = len - n + 1
        prev = dummy
        curr = head

        i = 0
        while i<dl-1:
            curr = curr.next
            prev = prev.next
            i += 1
        
        prev.next = prev.next.next

        return dummy.next
        