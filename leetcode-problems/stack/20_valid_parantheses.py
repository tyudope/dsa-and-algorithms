"""20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""


def isValid( s: str) -> bool:

        pairs = {')':'(', "]":"[",  "}":"{"}

        stack = []


        for b in s:
            if b in ("(", "[", "{"):
                stack.append(b)
            elif b in (")", "]", "}"):
                if not stack:
                    return False
                else:
                    if stack.pop() != pairs[b]:
                        return False

        return not stack



"""
Approach:
    Stack of opening brackets. Each closing bracket must match the most recent unmatched open (LIFO).
    Mismatch or empty stack on close -> invalid.
    Valid only if the stack is empty at the end.


Time: O(n) - one pass over the string.
Space: O(n) - worst case all opens e.g. "(((("
"""

