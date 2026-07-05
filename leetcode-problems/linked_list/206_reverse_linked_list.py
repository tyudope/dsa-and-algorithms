"""
LeetCode: 206 Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

"""
from typing import Optional
from ListNode import ListNode
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    curr = head
    prev = None
    next = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    head = prev
    return head


five = ListNode(5)
four = ListNode(4,five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
        

test = reverseList(one)
print(test.val)


