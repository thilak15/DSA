# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        slow.next=None
        head1, head2 = head, prev
        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            if temp1 is not None:  
                head2.next = temp1
            
            head1 = temp1
            head2 = temp2
    #Traverse to the middle of the list using two pointers
    # Reverse the second half of the list
    # merge th two lists
    # TIme complexity O(n)
    # space Complexity O(1)
    

