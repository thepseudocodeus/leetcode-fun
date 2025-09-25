Mathematical Language Cheatsheet for Problem Definition

1. Sequences vs Sets
   Term Definition LeetCode Example
   Sequence / List Ordered collection; duplicates allowed. Merge Two Sorted Lists (21)
   Set Unordered collection; duplicates not allowed. Contains Duplicate (217)
   Multiset Unordered collection; duplicates allowed. Top K Frequent Elements (347)

Practice Tip: Before coding, ask: Does order matter? Are duplicates allowed?

2. Monotonicity
   Term Definition Example
   Strictly Increasing a[i] < a[i+1] Longest Increasing Subsequence (300)
   Non-decreasing a[i] <= a[i+1] Merge Two Sorted Lists (21)
   Strictly Decreasing / Non-increasing a[i] > a[i+1] / a[i] >= a[i+1] Daily Temperatures (739) Monotonic Stack

Practice Tip: Identify monotonic patterns to apply two-pointer, binary search, or stack optimizations.

3. Intervals
   Term Definition Example
   Interval [start, end) or [start, end] Meeting Rooms (252)
   Disjoint Intervals No overlap Insert Interval (57)
   Overlap Intervals share points Merge Intervals (56)

Practice Tip: Draw intervals on a number line; precise overlap rules avoid edge case bugs.

4. Graph / Network Terms
   Term Definition Example
   Node / Vertex Point in a graph Number of Islands (200)
   Edge Connection between nodes Clone Graph (133)
   Connected Component Maximal set of connected nodes Number of Connected Components (323)
   Directed / Undirected Directional edges matter Course Schedule (207) vs Island Bridges

Practice Tip: Write relationships as functions or sets for clarity.

5. Functions & Mappings
   Term Definition Example
   Function Each input maps to exactly one output Two Sum (1)
   Injective / One-to-One Distinct inputs → distinct outputs Two Sum variation
   Surjective / Onto All outputs covered Range Mapping in Scheduling
   Monotone Function f(x) preserves order Binary Search (704)
6. Substructures
   Term Definition Example
   Subsequence Can skip elements, order preserved LIS (300)
   Subarray / Contiguous Consecutive elements Maximum Subarray (53)
   Prefix / Suffix Start/end portion of sequence Prefix Sum (560, 325)

Practice Tip: Always specify if subsequence must be contiguous.
