# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        def reverse(head: Optional[ListNode]):
            prev, curr = None, head
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        head1, head2 = head, reverse(slow.next)
        slow.next = None

        while head2:
            t1, t2 = head1.next, head2.next
            head1.next, head2.next = head2, t1
            head1, head2 = t1, t2
            