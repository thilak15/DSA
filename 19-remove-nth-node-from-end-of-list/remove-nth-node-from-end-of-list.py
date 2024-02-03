# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while n>0:
            right=right.next
            n-=1
        while right:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next

        # In the above approach we use two pointer concept=, Here we move the right pointer n times a head of the left pointer so when right pointer reaches the end left pointer is eaxctly before the N the pointer from the end
        # Time Complexity O(N)
        # Space Comeplexity O(1)