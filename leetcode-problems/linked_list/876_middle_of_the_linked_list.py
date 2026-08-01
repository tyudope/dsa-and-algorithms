"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""



"""

Tortoise-Hare Algorithm

Two-pointer idea:


"""



from ListNode import ListNode


def middleNode(head:ListNode) -> ListNode:

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


"""
Approach:

    Slow/fast pointers. Fast moves 2 steps per 1 of slow, so when fast reaches the end,
    slow is at the middle (second middle if even length).

Time: O(n) - single pass, fast traverses whole list.
Space: O(1) - two pointers, no extra structure.
"""

