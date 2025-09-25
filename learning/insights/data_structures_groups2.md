LeetCode Abstraction Map
1️⃣ Arrays

Conceptual: Sequence of elements, order matters, random access

Operations:

Access by index → O(1)

Append at end → O(1) amortized

Remove/insert at front/middle → O(n)

When to use: Fixed-size or bounded sequences; need index-based operations

2️⃣ Linked Lists

Conceptual: Sequence of nodes with pointers; dynamic size

Operations:

Insert/remove at head/tail → O(1)

Traversal from head → O(n)

Doubly linked list → traverse forward/backward

Pointers to maintain: head, tail, current

When to use: Frequent insertion/removal at known nodes; queues; deques

3️⃣ Stack (LIFO)

Reasoning: Temporal order → last-in-first-out

Implementation: Array end or DLL head

Operations: push/pop → O(1)

Use case: DFS, undo operations, parenthesis matching

4️⃣ Queue (FIFO)

Reasoning: Temporal order → first-in-first-out

Implementation: DLL head/tail or circular buffer

Operations: enqueue/dequeue → O(1)

Use case: BFS, sliding window, rate-limiting

5️⃣ Deque

Reasoning: Double-ended queue; access from both ends

Implementation: DLL or circular buffer

Operations: push/pop front/back → O(1)

Use case: Monotonic queues, sliding window max/min

6️⃣ HashMap / Hash Table

Reasoning: Key-based lookup → “structural access”

Implementation: Array of buckets + linked list per bucket

Operations: insert/find/delete → O(1) average

Use case: Caching, memoization, counting, grouping

7️⃣ LRU Cache

Reasoning: Temporal stack (usage order) + structural map

Implementation: HashMap (key → DLL node) + DLL to track order

Operations:

Access → O(1) via HashMap, move node to head

Insert → O(1) via DLL and HashMap

Evict least recently used → O(1) via tail pointer

Use case: Memoization, cache optimization

8️⃣ Trees / Graphs

Conceptual: Nodes connected via edges; generalized structure

Operations: DFS/BFS traversal, insert/delete, path queries

Specialized forms: BST, heap, trie, DAG

Use case: Hierarchical data, priority queues, connectivity, shortest path

9️⃣ General Principle

Reasoning perspective vs implementation:

Temporal reasoning (stack, queue, LRU order) → helps model problem logic

Structural implementation (arrays, DLL, hashmap) → makes operations O(1)

Key strategy: Always map problem’s invariant / access pattern → best abstract data structure → implementation that guarantees O(1)/O(log n) performance

10️⃣ Quick Reference Table
Abstraction Base Structure Temporal Reasoning Access / Insert Notes
Stack Array end / DLL head LIFO O(1) push/pop DFS, undo
Queue DLL head/tail / Circular buffer FIFO O(1) enqueue/dequeue BFS, sliding window
Deque DLL / Circular buffer Double-ended O(1) push/pop front/back Monotonic queue
HashMap Array + bucket list Key → structural O(1) avg insert/find/delete Caching, counting
LRU Cache HashMap + DLL Temporal + structural O(1) access, insert, evict Memoization, cache
Doubly Linked List DLL Forward/backward O(1) insert/remove at head/tail Queue, deque, cache nodes
