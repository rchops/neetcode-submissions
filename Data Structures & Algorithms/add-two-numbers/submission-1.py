# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers for each list
        # add vals - if < 10 add one node to new list
        # if >= 10 turn num into string - first int becomes node in string
        # second is passed on as carry
        curr1, curr2 = l1, l2
        carry = 0
        carry_case = False
        dummy = ListNode()
        ans = dummy
        while curr1 and curr2:
            if carry_case:
                val = curr1.val + curr2.val + carry
            else:
                val = curr1.val + curr2.val
            carry = 0
            carry_case = False
            if val < 10:
                ans.next = ListNode(val)
                ans = ans.next
            else:
                val_str = str(val)
                ans.next = ListNode(int(val_str[1]))
                ans = ans.next
                carry = int(val_str[0])
                carry_case = True

            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            if carry_case:
                val = curr1.val + carry
            else:
                val = curr1.val
            carry = 0
            carry_case = False
            if val < 10:
                ans.next = ListNode(val)
                ans = ans.next
            else:
                val_str = str(val)
                ans.next = ListNode(int(val_str[1]))
                ans = ans.next
                carry = int(val_str[0])
                carry_case = True
            
            curr1 = curr1.next
        
        while curr2:
            if carry_case:
                val = curr2.val + carry
            else:
                val = curr2.val
            carry = 0
            carry_case = False
            if val < 10:
                ans.next = ListNode(val)
                ans = ans.next
            else:
                val_str = str(val)
                ans.next = ListNode(int(val_str[1]))
                ans = ans.next
                carry = int(val_str[0])
                carry_case = True

            curr2 = curr2.next

        # if both lists are done and still carry append to end
        if carry_case:
            ans.next = ListNode(carry)

        return dummy.next