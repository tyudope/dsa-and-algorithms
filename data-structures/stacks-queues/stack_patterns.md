# Stack Patterns

Transferable techniques for stack problems. Organized by pattern, with problems as examples underneath.
per-problem rationale lives in each solution file; this is the pattern index.

---

### Matching / Nesting

Use a stack to track `open` items that are waiting to be closed.
Each closing item must match the most recent unmatched open (LIFO order).

**Core Idea**: push opens onto the stack. On a close, the top of the stack must be its matching open pop and compare.
Valid only if the stack is empty at the end (everything opened got closed).

**Why a stack**: nesting is inherently last-in-first-out the most recently opened bracket is the first that must close.
That is exactly stack order.


**Watch out for**:

 - Close with an empty stack -> invalid immediately (nothing to match).
 - Mismatch on top -> invalid immediately; don't wait for the end.
 - Combine both failure checks with short-circuit: not stack or stack.pop() != pairs[b]. If the stack is empty, pop() is never evaluated.
 - A dict {close: open} replaces a chain of near-identical if-blocks.


**Used in**:

 - 20 - Valid parantheses
 - 921 - Minimum Add to Make parentheses valid.
 - 1021 - Remove Outermost parentheses



---

### Monotonic Stack

Keep the stack in sorted order (increasing or decreasing) by popping elements that violate
the order before pushing. Answers "next greater/smaller element" questions in O(n).

**Core Idea**: before pushing the current element, pop everything that it "beats" (e.g.
everything smaller, for a next-greater problem). Each popped element has just found its answer
the current element.

**Why it works**:

each element is pushed and popped at most once, so the whole pass is O(n) despite the while loop.

**Watch out for**

 - Store indices, not values, when you need distances/positions.
 - Decide increasing vs decreasing based on wheter you want next-greater or next-smaller.



**Used in**:
 - 496 - Next Greater Element I
 - 739 - Daily temperatures
 - 84 - Largest Rectangle in histogram

