# Queue Patterns

Transferable techniques for queue problems.
Organized by pattern, with problems as examples underneath.
Per-problem rationale lives in each solution file; this is the pattern index.



---

## Simulate a Queue with Two Stacks

Build a FIFO structure out of two LIFO stakcs by exploiting orde reversal: reversing a reversed sequence gives back the original order

**Core Idea**: keep an `in_stack` and an `out_stack`


 - **enqueue/push** -> always onto `in_stack`. O(1)
 - **dequeue/pop** -> the oldest element is at the bottom of `in_stack` (worst stop in a LIFO). If `out_stack` is empty, pour all of `in_stack` into `out_stack` popping from one and pushing to the other reverses the order, so the oldest elemnt ends up on top of `out_stack`. Then pop `out_stack`.


 **The efficiency insight**: only transfer when `out_stack` is empty. If it still holds elements, they're already in correct FIFO order pop directly, no transfer. Each element moves between stacks at most once.

 **Why amortized O(1)**: a single dequeue that triggers a transfer is O(n) (every element moves). But that one transfer power many cheap pops afterward. so averaged over a sequence of operations the cost per operation is O(1). Same averaging idea as dynamic-array doubling. occasionally expensive, cheap on average. State it as "amortized O(1)", not flat "O(1)

**Watch out for**

 - Empty() must check BOTH stacks an element can sit in either one.
 - Bind stacks to `self` in `__init__` (`self.in_stack = []`) not as locals.
 - `pop` and `peek` share the identical transfer step factor it into a helper so a fix lands in one place.


**Used In**
 - 232 - Implement Queue using Stacks


***
## BFS (Breadth-First Search)

The queue's main appearance in problem-solving: explore level by level, oldest frontier node first.

**Watch out for**

 - Use `collection.deque` with `popleft`. NOT a list with `pop(0)` `pop(0)` is O(n) and turns on O(V+E) traversal quadratic.


 **Used in**

  - 102 - Binary Tree Level Order Traversal
  - 994 - Rotting Oranges
  - 200 - Number of Islands (grid BFS variant)



