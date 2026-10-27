# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tmp = dummy
        size = 0

        while head:
            size += 1
            head = head.next

        counter = 0

        while counter < size - n:
            counter += 1
            tmp = tmp.next

        tmp.next = tmp.next.next

        return dummy.next