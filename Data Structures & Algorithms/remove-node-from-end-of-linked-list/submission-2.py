# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use one pointer to go to end
        end = head
        length = 0
        while end:
            end = end.next
            length = length + 1

        # another pointer goes through and counts down
        curr, prev = head, None
        dist = 0
        while curr and (length - dist) > n:
            prev = curr
            curr = curr.next
            dist = dist + 1

        # remove when get to right node change links
        # if prev = None - remove curr
        # head = head.next
        if prev:
            prev.next = curr.next
        else:
            head = head.next

        return head