6️⃣ General Statement

Graphs = universal abstraction

Nodes = elements

Edges = relationships or pointers

Most data structures can be seen as graphs with constraints:

Linked list → path

Array → path with implicit edges via indices

Tree → acyclic directed graph

HashMap → graph of keys → nodes in buckets

1️⃣ Time vs Access Perspective

Conceptually, the structure behaves like a stack (or queue) in “usage order”:

Most recently accessed item → “top” of the stack (head of DLL)

Least recently used item → “bottom” (tail of DLL)

But in practice, we don’t traverse the stack to find the item, because:

HashMap gives direct access by key (O(1))

So the time-ordering is tracked separately in the DLL

2️⃣ HashMap + DLL = O(1) Efficient Operations
Operation How it works Time Complexity
Access item Lookup key in HashMap → node in DLL → move node to head O(1)
Insert item Add node to head of DLL + key → node in HashMap O(1)
Evict least-recently-used Remove tail node of DLL + remove from HashMap O(1)

Key idea: Time-order stack is abstracted in DLL; direct access is enabled by HashMap.

3️⃣ Mental Model
Time-order stack (conceptual):
MRU → ... → LRU

Implementation:
HashMap: key → DLL node
DLL: head = MRU, tail = LRU

When we want an item:

Use HashMap → O(1) access

Update DLL → maintain stack-like usage order

We never “walk the stack” to find the item → optimal access.

4️⃣ Takeaway

We are reasoning temporally: stack of recent usage.

We are implementing structurally: HashMap + DLL.

This is the pattern behind LRU caches, memoization, and many high-performance algorithmic designs.
