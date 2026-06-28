# Data Structures & Algorithms

A long-term, foundation-first study log. The goal is not coverage or problem count — it's understanding each structure deeply enough to explain its tradeoffs cold, and to know when it's the *wrong* choice.

Two tracks run in parallel:

- **Daily LeetCode (1/day):** maintenance reps. Pulled from the topic currently being studied or already covered — never from material not yet reached. Keeps recall warm.
- **Weekly deep study (3–4h):** the actual foundation. One topic, studied properly, implemented from scratch, notes that pass the five-question bar below.

## The depth standard

Every structure's `notes.md` must answer all five before it counts as "done":

1. What problem does this exist to solve?
2. What are the core operations and their complexities?
3. What's the key tradeoff vs. the alternatives?
4. When is this the *wrong* choice?
5. One real-world / systems use.

If the notes only list operations, it's copied, not learned.

## Repo structure

```
dsa/
├── README.md              # this file
├── data-structures/       # implement from scratch, then notes.md
├── algorithms/
├── patterns/
└── leetcode-problems/     # each: solution + README with rationale
```

Every solved problem gets a written rationale: brute force → bottleneck → unlocking insight → final time/space complexity.

## Progress tracker

Pace: ~3–4h deep study/week + 1 LeetCode/day. Full track ≈ 19–23 weeks. Mark `[x]` when the five-question bar is met, not when the code merely runs.

### Foundations

- [ ] **W1 — Arrays + dynamic array from scratch.** Resizing, amortized cost. *(LC: easy arrays to start the streak, in-place ops)*
- [ ] **W2 — Linked lists.** Singly + doubly, both implemented. *(LC: reversal, cycle detection, merge)*
- [ ] **W3 — Stacks & queues.** Implemented on array *and* linked list. *(LC: valid parens, min-stack, queue-from-stacks)*

### Hashing & core patterns

- [ ] **W4 — Hash tables pt.1.** Hashing, collisions (chaining vs. open addressing). *(LC: two-sum family, frequency counts)*
- [ ] **W5 — Hash tables pt.2.** Load factor, resizing; implement one. *(LC: grouping, dedup, set logic)*
- [ ] **W6 — Recursion + two-pointer / sliding-window.** *(LC: two pointers, window problems)*
- [ ] **W7 — Binary search.** The pattern, not just the array case. *(LC: search variants, rotated arrays)*

### Trees

- [ ] **W8 — Trees pt.1.** Binary trees, traversals (pre/in/post/level). *(LC: traversal problems)*
- [ ] **W9 — Trees pt.2 (BST).** Insert, search, delete; invariants. *(LC: BST validation, kth-smallest)*
- [ ] **W10 — Balanced trees.** AVL / red-black *conceptually* — rotations and why. *(LC: depth/balance problems)*

### Heaps

- [ ] **W11 — Heaps.** Binary heap, sift up/down; implement one. *(LC: top-K, merge-K, median stream)*
- [ ] **W12 — Priority queues + applications.** *(LC: scheduling-style problems)*

### Graphs

- [ ] **W13 — Graphs pt.1.** Representations (adj list vs. matrix), tradeoffs. *(LC: build/traverse small graphs)*
- [ ] **W14 — Graphs pt.2.** BFS + DFS, both implemented. *(LC: connected components, flood fill)*
- [ ] **W15 — Graphs pt.3.** Shortest path (Dijkstra), topological sort. *(LC: grid shortest-path, course schedule)*

### Paradigms

- [ ] **W16 — Divide & conquer.** Merge sort, quicksort from scratch. *(LC: sorting-based problems)*
- [ ] **W17 — Greedy.** When it works, when it silently fails. *(LC: interval problems)*
- [ ] **W18 — DP pt.1.** Memoization, 1D cases. *(LC: climbing stairs, house robber)*
- [ ] **W19 — DP pt.2.** 2D / grid DP. *(LC: grid paths, edit distance)*
- [ ] **W20 — DP pt.3.** Knapsack family, subsequence problems. *(LC: LIS, coin change)*
- [ ] **W21 — Backtracking.** The template, pruning. *(LC: permutations, subsets, N-queens)*

### Consolidation

- [ ] **W22–23 — Consolidation.** Re-implement weak structures, write summary notes. *(LC: mixed review, spaced repetition across past topics)*

## Reference

- *The Algorithm Design Manual* (Skiena) — narrative, motivates *why* before *how*.
- *Introduction to Algorithms* (CLRS) — the reference; heavier, proof-dense.

## Log

| Date | LC problem | # | Topic week | Notes |
|------|-----------|---|------------|-------|
| | | | | |
