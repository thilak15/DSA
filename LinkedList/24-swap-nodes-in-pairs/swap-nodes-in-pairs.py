# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head

        prev = dummy
        while head and head.next:
            first=head
            second=head.next

            # swapping
            prev.next=second
            first.next=second.next
            second.next=first

            prev=first
            head=first.next
        return dummy.next
        # Time complexity O(N)
        # Space complexiyt O(1)

