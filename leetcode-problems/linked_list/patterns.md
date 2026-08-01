
# Linked List - Patterns

Transferable techniques for linked-list problems. Organized by pattern, with problems as examples underneath. Per-problem rationale lives in each solution file; this is the pattern index.



---

### Slow / Fast Pointers (Tortoise-Hare)

Two pointers walk the list; fast moves 2 steps for every 1 of slow.

**Core Idea**: fast covers the list at double speed, so when fast reaches the end, slow has covered exactly half it sits at the middle.


**Why it works**: distance(fast) = 2 * distance(slow). When fast is at the end(distance n), slow is at n/2

**Watch out for**:

- Loop condition `while fast and fast.next` order matters. Checking `fast` first short-circuits so `fast.next` is never evaluated on a `None`, avoiding AttributteError.
- Even-length lists have two middles. `while fast and fast.next` lands on the **second** middle; `while fast.next and fast.next.next` lands on the first. The control condition decides which.


**Used in**

- 876 - Middle of the Linked List
- 141 - Linked List Cycle (fast catches slow if a cycle exists)
- Finding the nth node from the end (offset the two pointers)
